import requests
import logging
import sys
from urllib3.exceptions import InsecureRequestWarning
import sys
from kinesis import stream_put
from params import *
from database_connect import *
from datetime import datetime, timedelta
import json
import inflection



api_token = 'jGGycwV_ujHc6E7nShV9'
headers = {'api-token': api_token}
base_url = 'https://sfo-nyansa.flysfo.com/graphql'
fmt = '%(asctime)s %(message)s'
logging.basicConfig(filename='nyansa_collector.log', level=logging.DEBUG, format=fmt)
handler = logging.StreamHandler()
handler.terminator = ""
logger = logging.getLogger(__name__)

def execute(query):
    try:
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        r = requests.post(url=base_url, json=query, headers=headers, verify=False)
        if r.status_code ==200:
            return r.json()
        else:
            raise Exception("Failed to execute query with return code {}".format(requests.status_code))
    except requests.exceptions.HTTPError as err:
        logger.error(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        logger.error(err)
        print(err)
        sys.exit(1)


def main(args):
    # print(sys.path)
    # topic = kinesis_topics()
    # publish to kinesis
    # stream_put(topic.ap, result)
    #qy = get_query()
    total = 0

    if args[1]=='ap':
        #Access Points
        # ap_result = execute(qy.ap)
        #1071

        for n in range(1,23):
            ap_str={"variables": {"from_Date": "2018-07-01", "to_Date": "2018-08-30", "page_size": 50, "page_num": 1} ,"query": "query testQueryName($from_Date:String, $to_Date:String, $page_size:Int, $page_num:Int) {  accessPointList(fromDate:$from_Date, toDate:$to_Date, pageSize:$page_size, page:$page_num) { page pageCount pageSize totalCount accessPoints { apGroup apLocation apModel apName controllerDescription controllerIp controllerModel controllerSerialNum controllerVersion createdAt description ipAddress lastApRebootReason lastUpdated numDevices uuid voyanceUrl apRadios { adminStatus essids numDevices radioChannel radioHtMode radioMode radioNoiseFloor radioPhyType rfBand rfProtocol rfChannelWidth txPowerLevel }  }}}"}
            ap_str["variables"]["page_num"]=n
            print(ap_str)
            ap_result=execute(ap_str)
            print(ap_result)
            if ap_result != None:
                total=total+dbconnect_ap(ap_result['data']['accessPointList']['accessPoints'])
        print(print("%d records created!" %total))



    elif args[1]=="server":
        #Servers
        #6282,130pgs
        server_str = {"variables": {"fromDate": "2018-08-12", "toDate":"2018-08-13", "page_size": 50, "page_num":1},
                       "query": "query testQueryName($fromDate: String){  serverList(fromDate: $fromDate) {  servers{ ipAddress dnsHostname serverTypes uuid  voyanceUrl createdAt lastUpdated relatedClients { clients{apDwellTimeMs apGroup apMacAddr browser bssid chWidth class controllerIp createdAt dnsHostname essid ipAddress is5ghzCapable isActive isDfsCapable isOnDualBandAp isWireless lastUpdated macAddress model network noiseOnAp os osAndVersion protocol radioChannel radioNumber radioTechType rfBand snr source userAgent userName uuid voyanceUrl }}}}}"}

        for n in range(1,2):
            server_str["variables"]["page_num"] = n
            # print(server_str)
            sv_result = execute(server_str)
            print(sv_result)
            if sv_result != None:
                total=total+dbconnect_server(sv_result['data']['serverList']['servers'])

        print("{} records created!!!".format(total_count))

    elif args[1] == "device":
    # Devices
    # ''' from_Date: current date time in utc - 2 minutes
    #     to_Date: current date time in utc
    #     page_size: 50
    # '''
        device_query_str= {"variables": {"from_Date": "2018-08-12", "to_Date":"2018-08-13","page_size":50, "page_num":1}, "query": "query testQueryName($from_Date: String, $to_Date: String, $page_size:Int, $page_num:Int) { deviceList(fromDate:$from_Date, toDate:$to_Date,pageSize:$page_size, page:$page_num) { totalCount clients { apDwellTimeMs apGroup apMacAddr browser bssid chWidth class controllerIp createdAt dnsHostname essid ipAddress is5ghzCapable isActive isDfsCapable isOnDualBandAp isWireless lastUpdated macAddress model network noiseOnAp os osAndVersion protocol radioChannel radioNumber radioTechType rfBand snr source userAgent userName uuid voyanceUrl }}}"}
        start_time='{:%Y-%m-%d %H:%M:%S+0000}'.format(datetime.utcnow() - timedelta(minutes=5))
        end_time='{:%Y-%m-%d %H:%M:%S+0000}'.format(datetime.utcnow())
        device_query_str["variables"]["from_Date"]=start_time
        device_query_str["variables"]["to_Date"]=end_time
        device_total = execute(device_query_str)
        page_count=round(device_total["data"]["deviceList"]["totalCount"]/50)
        total_count=0
        print(device_query_str)
        for n in range(1,page_count):

            device_query_str["variables"]["page_num"]=n
            # print(device_query_str)
            device_result = execute(device_query_str)

            if device_result != None:
                # dbconnect_device(device_result["data"]["deviceList"]["clients"])
                total_count=total_count+dbconnect_device(device_result["data"]["deviceList"]["clients"])
        print("device total shows {}".format(device_total))
        print("total {} records created from {} to {}!!!".format(total_count,start_time,end_time))
    # logger.info("end")
    else:
        print("unknown arg, pass either ap or server or device")

if __name__ == '__main__':
    main(sys.argv)


    #ap_query1={"query": "query testQueryName { accessPointList { accessPoints { apGroup apLocation apModel apName controllerDescription controllerIp controllerModel controllerSerialNum controllerVersion createdAt description ipAddress lastApRebootReason lastUpdated numDevices uuid voyanceUrl apRadios { adminStatus essids numDevices radioChannel radioHtMode radioMode radioNoiseFloor radioPhyType rfBand rfProtocol txPowerLevel } }}}"}
