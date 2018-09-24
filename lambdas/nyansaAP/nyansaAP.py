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
        # payload = base64.b64decode(record['data']).decode('utf-8')
        payload=base64.b64decode(record["kinesis"]["data"]).decode('utf-8')
        jsonr = json.loads(str(payload))
        #ap_result = jsonr['data']['accessPointList']['accessPoints']
        if jsonr !=None:
            dbconnect_ap(jsonr)
        print("===ap and radio records created!===")


def dbconnect_ap(result):
    try:
        conn = psycopg2.connect(host=dbinit["host"], port=dbinit["port"], dbname=dbinit["dbname"], user=dbinit["user"],
                                password=dbinit["password"], connect_timeout=dbinit["timeoutmin"])
        cursor = conn.cursor()
        x = 0
        y = 0
        aps = keyterator(result['data']['accessPointList']['accessPoints'], inflection.underscore)
        
        for ap in aps:
            radio_list = ap["ap_radios"]
            del ap["ap_radios"]
            ap_columns = ap.keys()
            ap_values = ["None" if ap[column] is None else ap[column] for column in ap_columns]
            insert_stmt = "insert into nya_ap ({}) values {}".format(AsIs(','.join(ap_columns)), tuple(ap_values))

            try:
                cursor.execute(insert_stmt)
                x = x + 1
                conn.commit()
            except psycopg2.IntegrityError as err:
                conn.rollback()
                print(err)
                print("ap insert not pass, try update")
                update_stmt = "update nya_ap set ({}) = {} where uuid= '{}'".format(
                    AsIs(','.join(ap_columns)), tuple(ap_values), ap["uuid"])
                try:
                    cursor.execute(update_stmt)
                    x = x + 1
                    #print(radio_list)
                    y = y + dbconnect_radio(conn,radio_list,ap)
                except psycopg2.IntegrityError as err:
                    conn.rollback()
                    print(err)
                    print(update_stmt)
                    print("ap update not pass, rollback")
            conn.commit()

        
        print("{} aps, {} radios created!".format(x, y))
    
    except psycopg2.Error as err:
        print("some psycopg2 exception:")
        print(err)
    except Exception as err:
        print("some exception:")
        print(err)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def dbconnect_radio(conn,result,ap):
    try:
        cursor = conn.cursor()
        y = 0
        ap_radios = keyterator(result, inflection.underscore)
        for apr in ap_radios:
            essids_lst = apr["essids"]
            apr["essids"] = ",".join(essid for essid in essids_lst)
            apr.update({"ap_ip_address": ap["ip_address"], "ap_created_at": ap["created_at"],
                        "ap_last_updated": ap["last_updated"]})
            apr_columns = apr.keys()
            apr_values = ["None" if apr[column] is None else apr[column] for column in apr_columns]

            insert_stmt = "insert into nya_ap_radios ({}) values {}".format(AsIs(','.join(apr_columns)),tuple(apr_values))
                                                               
            try:
                cursor.execute(insert_stmt)
                conn.commit()
                y = y + 1

            except psycopg2.IntegrityError as err:
                conn.rollback()
                print(err)
                print("radio insert not pass, try update")
                update_stmt = "update nya_ap_radios set ({}) = {} where ap_ip_address='{}' and radio_channel='{}'".format(
                    AsIs(','.join(apr_columns)), tuple(apr_values), ap["ip_address"], apr["radio_channel"])
                try:
                    cursor.execute(update_stmt)
                    y = y + 1
                    conn.commit()
                except psycopg2.IntegrityError as err:
                    conn.rollback()
                    print(err)
                    print(update_stmt)
                    print("radio update not pass, rollback")
        print("{} ends! {} records created".format("radio",y))   
    except psycopg2.Error as err:
        print("some psycopg2 exception:")
        print(err)
    except Exception as err:
        print("some exception")
        print(err)
    return y
