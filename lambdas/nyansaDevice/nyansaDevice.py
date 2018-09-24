from __future__ import print_function
from helper import keyterator
import psycopg2
from psycopg2.extensions import AsIs
import json
import base64
import inflection
import re

dbinit = ({"host": "dev-postdb02.cmq2evoherht.us-west-2.rds.amazonaws.com"
              , "dbname": "devpostdb02", "user": "tis_pwifi", "password": "PWiFidev2tek@p0$t"
              , "timeoutmin": 5, "port": "5432",
           })
def lambda_handler(event, context):
    for record in event['Records']:
       #Kinesis data is base64 encoded so decode here
        payload=base64.b64decode(record["kinesis"]["data"])
        pp=str(payload)
      
        pp=re.sub("^b'.*x01?","",pp)
        print(">>>>")
        if "deviceList" in pp:
            print(pp)

        # jsonr = json.loads(str())
        # print(json.dumps(jsonr))
        # if jsonr !=None:
        #     dbconnect_client(jsonr)
        # print("===client records created!===")


def dbconnect_client(result):
    try:
        conn = psycopg2.connect(host=dbinit["host"], port=dbinit["port"], dbname=dbinit["dbname"], user=dbinit["user"],
                                password=dbinit["password"], connect_timeout=dbinit["timeoutmin"])
        cursor = conn.cursor()
        # print(result)
        clients = keyterator(result['data']['deviceList']['clients'], inflection.underscore)

        x = 0
        for client in clients:
            client.update({"client_ip_address": client["ip_address"],
                           "ap_mac_address": client["ap_mac_addr"], "client_mac_address": client["mac_address"],
                           "client_uuid": client["uuid"], "client_voyance_url": client["voyance_url"]})
            del_keys = ("ip_address", "mac_address", "uuid", "voyance_url", "ap_mac_addr")
            for k in del_keys:
                if k in client:
                    del client[k]

            client_columns = client.keys()
            integer_check=["ap_dwell_time_ms","noise_on_ap","snr"]
            bool_check=["is5ghz_capable","is_active","is_dfs_capable","is_on_dual_band_ap","is_wireless"]
            for column in client_columns:
                if column in integer_check:
                    if client[column] is None:
                        client[column]=0
            for column in client_columns:
                if column in bool_check:
                    if client[column] is None:
                        client[column]=False
            client_values = ["None" if client[column] is None else client[column] for column in client_columns]
            insert_stmt = "insert into nya_clients1 ({}) values {}".format(AsIs(','.join(client_columns)), tuple(client_values))
            try:
               
                if client["ap_mac_address"] is None:
                    pass
                else:
                    print(client)
                    cursor.execute(insert_stmt)
                    x = x+1
            except psycopg2.IntegrityError as err:
                conn.rollback()
                print(err)
                print("client insert not pass, rollback")
            conn.commit()
        print("{} clients created!".format(x))
        return x
    except Exception as err:
        print(err)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()