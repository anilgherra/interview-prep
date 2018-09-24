from __future__ import print_function
from helper import keyterator
import psycopg2
from psycopg2.extensions import AsIs
import json
import base64
import inflection


dbinit = ({"host": "dev-postdb02.cmq2evoherht.us-west-2.rds.amazonaws.com"
              , "dbname": "devpostdb02", "user": "tis_pwifi", "password": "PWiFidev2tek@p0$t"
              , "timeoutmin": 5, "port": "5432",
           })
def lambda_handler(event, context):
    for record in event['Records']:
       #Kinesis data is base64 encoded so decode here
        payload=base64.b64decode(record["kinesis"]["data"]).decode('utf-8')
        jsonr = json.loads(str(payload))
        if jsonr !=None:
            dbconnect_server(jsonr)
        print("===server and clients records created!===")


def dbconnect_server(result):
    try:
        conn = psycopg2.connect(host=dbinit["host"], port=dbinit["port"], dbname=dbinit["dbname"], user=dbinit["user"],
                                password=dbinit["password"], connect_timeout=dbinit["timeoutmin"])
        cursor = conn.cursor()
        servers = keyterator(result["data"]["serverList"]["servers"], inflection.underscore)
        x = 0
        y = 0
        
        for server in servers:
            client_list = server["related_clients"]["clients"]
            del server["related_clients"]
            sv_type=server["server_types"]
            server["server_types"]=",".join( stype for stype in sv_type)
            server_columns = server.keys()
            server_values = ["None" if server[column] is None else server[column] for column in server_columns]
            insert_stmt = "insert into nya_server ({}) values {}".format(AsIs(','.join(server_columns)),
                                                                               tuple(server_values))
            try:
                cursor.execute(insert_stmt)
                conn.commit()
                x = x + 1
                y = y + dbconnect_server_client(conn, client_list, server["ip_address"])

            except psycopg2.IntegrityError as err:
                conn.rollback()
                print(err)
                print("server insert not pass, try update")
                update_stmt = "update nya_server set ({}) = {} where ip_address='{}'".format(
                    AsIs(','.join(server_columns)), tuple(server_values), server["ip_address"])
                try:
                    cursor.execute(update_stmt)
                    conn.commit()
                    x = x + 1
                except psycopg2.IntegrityError as err:
                    conn.rollback()
                    print(err)
                    print(update_stmt)
                    print("radio update not pass, rollback")
        print("{} server, {} clients created!!".format(x,y))
    except(Exception) as err:
        print(err)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def dbconnect_server_client(conn,result,server_ip):
    try:
        cursor = conn.cursor()
        clients = keyterator(result, inflection.underscore)
        y = 0
        
        for client in clients:
            client.update({"client_ip_address": client["ip_address"], "server_ip_address": server_ip,
                               "ap_mac_address": client["ap_mac_addr"], "client_mac_address": client["mac_address"],
                               "client_uuid": client["uuid"], "client_voyance_url": client["voyance_url"]})
            del_keys = ("ip_address", "mac_address", "uuid", "voyance_url", "ap_mac_addr")
            for k in del_keys:
                if k in client:
                    del client[k]

            client_columns = client.keys()

            for column in client_columns:
                if column=="ap_dwell_time_ms" or column=="noise_on_ap" or column=="snr":
                    if client[column] is None:
                        client[column]=0

            # client_values = [0 if column="ap_dwell_time_ms" is None or client[column]=="noise_on_ap" is None or client[column]=="snr" is None else client[column] for column in client_columns]
            client_values = ["None" if client[column] is None else client[column] for column in client_columns]
            insert_stmt = "insert into nya_server_client ({}) values {}".format(AsIs(','.join(client_columns)),tuple(client_values))
            try:
                if client["client_mac_address"] is None:
                    pass
                else:
                    cursor.execute(insert_stmt)
                    y = y + 1
            except psycopg2.IntegrityError as err:
                conn.rollback()
                print("server client insert not pass, rollback")
                print(err)
                print(update_stmt)
            conn.commit()
            print("{} sclients created!".format(y))
        return y
    except(Exception) as err:
        print(err)

