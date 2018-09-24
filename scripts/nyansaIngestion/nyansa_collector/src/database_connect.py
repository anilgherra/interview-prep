
import dataset
from helper import keyterator
import inflection
from sqlalchemy.exc import IntegrityError

def dbconnect_ap(result):

    try:
        db_init = dataset.connect(
            'postgresql://tis_pwifi:PWiFidev2tek@p0$t@dev-postdb02.cmq2evoherht.us-west-2.rds.amazonaws.com:5432/devpostdb02',
            schema='tis_pwifi')
        # tb_ap = db_init['nya_ap_ok']
        tb_radio=db_init['nya_ap_radios_ok1']
        #tb = db_init.create_table('nya_ap_ok',primary_id='ip_address',primary_type=db_init.types.text)

        i=0
        for ap in result:

            # ap_dic=({ "ap_group": ap["apGroup"],"ap_location": ap["apLocation"],"ap_model": ap["apModel"],
            #           "ap_name": ap["apName"],"controller_description": ap["controllerDescription"],"controller_ip": ap["controllerIp"],
            #           "controller_model": ap["controllerModel"],"controller_serial_num": ap["controllerSerialNum"],"controller_version": ap["controllerVersion"],
            #           "description": ap["description"],"ap_ip_address": ap["ipAddress"],"last_ap_reboot_reason": ap["lastApRebootReason"],
            #           "created_at": ap["createdAt"],"last_updated": ap["lastUpdated"],"num_devices": ap["numDevices"],
            #           "uuid": ap["uuid"],"voyance_url": ap["voyanceUrl"]})

            # try:
            #     i=i+1
            #     tb_ap.upsert(ap_dic, ["ap_ip_address"])
            # except(Exception) as err:
            #     print(err)

            ap_radios = keyterator(ap["apRadios"], inflection.underscore)
            for apr in ap_radios:
                essids_lst = apr["essids"]
                apr["essids"] = ",".join(essid for essid in essids_lst)
                apr.update({"ap_ip_address": ap["ipAddress"],"ap_created_at": ap["createdAt"],"ap_last_updated": ap["lastUpdated"]})
                try:
                        i=i+1
                        tb_radio.upsert(apr, ["ap_ip_address","radio_channel"])
                except(Exception) as err:
                        print(err)
        print("%d record created!" %i)
        return i
    except(Exception) as err:
        print(err)


def dbconnect_server(result):
    conn = None
    try:
        db_init = dataset.connect(
            'postgresql://tis_pwifi:PWiFidev2tek@p0$t@dev-postdb02.cmq2evoherht.us-west-2.rds.amazonaws.com:5432/devpostdb02',
            schema='tis_pwifi')
        tb_server = db_init["nya_server_ok"]
        tb_client = db_init["nya_server_client_ok"]
        # tb_server = db_init.create_table('nya_server_ok',primary_id='ip_address',primary_type=db_init.types.text)
        # tb_client = db_init.create_table('nya_server_client_ok')

        i=0
        for server in result:
            # sv_type=server["serverTypes"]
            # server["serverTypes"]=",".join( stype for stype in sv_type)
            # server_dic=({"ip_address":sv["ipAddress"],"dns_host_name":sv["dnsHostname"],"server_types":sv["serverTypes"],"uuid":sv["uuid"],"voyance_url":sv["voyanceUrl"],"created_at":sv["createdAt"],"last_updated":sv["lastUpdated"]})
            # print(server_dic)
            # try:
            #     print("start")
            #     tb_server.upsert(server_dic,["ip_address"],ensure=True)
            #     print("done")
            # except(Exception) as err:
            #         print(err)




            devices = keyterator(server["relatedClients"]["clients"], inflection.underscore)
            print(devices)
            for device in devices:
                #To Do: change sv["ipAddress"] to sv["ip_address"] when use key iterator
                device.update({"server_ip_address": sv["ipAddress"],"client_ip_address":device["ip_address"],"ap_mac_address":device["ap_mac_addr"],"client_mac_address":device["mac_address"],"client_uuid":device["uuid"],"client_voyance_url":device["voyance_url"]})
                del_keys=("ip_address","mac_address","uuid","voyance_url","ap_mac_addr")
                for k in del_keys:
                    if k in device:
                        del device[k]
                # del svc["ip_address"]
                # del svc["mac_address"]
                # del svc["uuid"]
                # del svc["voyance_url"]
                # del svc["ap_mac_addr"]
                print(device)
                try:
                    i = i + 1
                    tb_client.insert(device,["client_mac_address,last_updated"])
                except(Exception) as err:
                    print(err)
        print("%d record created!" % i)
        return i
    except(Exception) as err:
        print(err)



def dbconnect_device(result):
    try:
        db_init = dataset.connect(
            'postgresql://tis_pwifi:PWiFidev2tek@p0$t@dev-postdb02.cmq2evoherht.us-west-2.rds.amazonaws.com:5432/devpostdb02',
            schema='tis_pwifi')
        tb = db_init.create_table('nya_client_ok')

        devices=keyterator(result,inflection.underscore)

        i=0
        for device in devices:
            device.update({"client_ip_address": device["ip_address"],
                           "ap_mac_address": device["ap_mac_addr"], "client_mac_address": device["mac_address"],
                           "client_uuid": device["uuid"], "client_voyance_url": device["voyance_url"]})
            del_keys = ("ip_address", "mac_address", "uuid", "voyance_url", "ap_mac_addr")
            for k in del_keys:
                if k in device:
                    del device[k]

            try:
                i=i+1
                tb.insert(device)
            except(IntegrityError) as err:
                pass
            except(Exception) as err:
                print(err)
        print("{} record created!".format(i))
        return i
    except(Exception) as err:
        print(err)