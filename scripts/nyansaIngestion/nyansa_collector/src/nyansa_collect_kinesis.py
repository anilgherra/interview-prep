import requests
import logging
import sys
from urllib3.exceptions import InsecureRequestWarning
from datetime import datetime, timedelta
from kinesis import stream_put

api_token = "jGGycwV_ujHc6E7nShV9"
headers = {"api-token": api_token}
base_url = "https://sfo-nyansa.flysfo.com/graphql"
fmt = "%(asctime)s %(message)s"
logging.basicConfig(filename=r"/sfo/nyansa_collector.log", level=logging.DEBUG, format=fmt)
handler = logging.StreamHandler()
handler.terminator = ""
logger = logging.getLogger(__name__)

ap = {"variables": {"fromDate": "2018-07-19 00:00:00+0000","pageSize": 50,"page": 1,"sortBy": "uuid"},
      "query": "query testQueryName($fromDate:String,$pageSize:Int,$page:Int,$sortBy:String)  { "
               "accessPointList(fromDate:$fromDate,pageSize:$pageSize,page:$page,sortBy:[$sortBy]) {  pageCount  accessPoints { apGroup apLocation apModel apName controllerDescription controllerIp "
               "controllerModel controllerSerialNum controllerVersion createdAt description ipAddress lastApRebootReason lastUpdated numDevices uuid voyanceUrl "
               "apRadios { adminStatus essids numDevices radioChannel radioHtMode radioMode radioNoiseFloor radioPhyType rfBand rfProtocol txPowerLevel } }}}"
      }

server = {"variables": {"fromDate": "2018-07-19 00:00:00+0000","toDate":"2018-08-27 00:00:00-0700","pageSize":50,"page": 1, "sortBy":"lastUpdated"},
          "query": "query testQueryName($fromDate:String,$toDate:String,$pageSize:Int,$page:Int,$sortBy:String){ "
                   "serverList(fromDate:$fromDate,toDate:$toDate,pageSize:$pageSize,page:$page,sortBy:[$sortBy]) {  pageCount servers{ ipAddress dnsHostname serverTypes uuid  voyanceUrl createdAt lastUpdated "
                   " relatedClients { clients{apDwellTimeMs apGroup apMacAddr browser bssid chWidth class controllerIp createdAt dnsHostname essid "
                   " ipAddress is5ghzCapable isActive isDfsCapable isOnDualBandAp isWireless lastUpdated macAddress model network noiseOnAp os osAndVersion "
                   " protocol radioChannel radioNumber radioTechType rfBand snr source userAgent userName uuid voyanceUrl}}}}}"
          }
device = {"variables": {"fromDate": "2018-08-12 00:00:00+0000", "toDate": "2018-08-13 00:00:00-0700","pageSize":50,"page": 1,"sortBy":"lastUpdated"},"query": "query testQueryName($fromDate:String,$toDate:String,$pageSize:Int,$page:Int,$sortBy:String) { deviceList(fromDate:$fromDate,toDate:$toDate,pageSize:$pageSize,page:$page,sortBy:[$sortBy]) { pageCount clients { apDwellTimeMs apGroup apMacAddr browser bssid chWidth class controllerIp createdAt dnsHostname essid ipAddress is5ghzCapable isActive isDfsCapable isOnDualBandAp isWireless lastUpdated macAddress model network noiseOnAp os osAndVersion protocol radioChannel radioNumber radioTechType rfBand snr source userAgent userName uuid voyanceUrl }}}"}


def execute(query):
    try:
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        r = requests.post(url=base_url, json=query, headers=headers, verify=False)
        if r.status_code == 200:
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
    print(args)
    env = args[2]
    if args[1] == 'ap':
        ap_result1 = execute(ap)
        # print(ap_result1)
        total_count = ap_result1["data"]["accessPointList"]["pageCount"]
        for n in range(1, total_count + 1):
            ap["variables"]["page"] = n
            if ap_result1 != None:
                ap_result2 = execute(ap)
                print(ap_result2)
                status=stream_put(env, 'aws-dev-nyansa-ap', ap_result2)
                logger.info("{}".format(status))
        logger.info("{} records sent!!!".format("ap"))

    elif args[1] == "server":
        start_time = '{:%Y-%m-%d %H:%M:%S+0000}'.format(datetime.utcnow() - timedelta(hours=24))
        end_time = '{:%Y-%m-%d %H:%M:%S+0000}'.format(datetime.utcnow())
        server["variables"]["fromDate"] = start_time
        server["variables"]["toDate"] = end_time
        server_result1 = execute(server)
        # print(server_result1)
        total_count = server_result1["data"]["serverList"]["pageCount"]
        for n in range(1, total_count + 1):
            server["variables"]["page"] = n
            if server_result1 != None:
                server_result2 = execute(server)
                print(server_result2)
                status=stream_put(env, 'aws-dev-nyansa-server', server_result2)
                logger.info("{}".format(status))
        logger.info("start_time={} end_time={}, {} records sent  !!!".format(start_time, end_time, "server"))

    elif args[1] == "device":
        start_time = '{:%Y-%m-%d %H:%M:%S+0000}'.format(datetime.utcnow() - timedelta(minutes=5))
        end_time = '{:%Y-%m-%d %H:%M:%S+0000}'.format(datetime.utcnow())
        device["variables"]["fromDate"] = start_time
        device["variables"]["toDate"] = end_time
        device_result1 = execute(device)
        print(device_result1)
        total_count = device_result1["data"]["deviceList"]["pageCount"]
        for n in range(1, total_count + 1):
            device["variables"]["page"] = n
            if device_result1 != None:
                device_result2 = execute(device)
                print(device_result2)
                status=stream_put(env, 'aws-dev-nyansa-device', device_result2)
                logger.info("{}".format(status))
        logger.info("start_time={} end_time={}, {} records sent  !!!".format(start_time, end_time, "device"))
    else:
        logger.info("unknown arg, pass ap or server or device")

if __name__ == '__main__':
    main(sys.argv)
