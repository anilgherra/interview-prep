#
# import psycopg2
#
#
# def dbconnect(result):
#     conn = None
#     try:
#         conn = psycopg2.connect(database="devpostdb02", user="tis_pwifi", password="PWiFidev2tek@p0$t",
#                                 host="dev-postdb02.cmq2evoherht.us-west-2.rds.amazonaws.com", port="5432")
#         cur = conn.cursor()
#         ap_list = result['data']['accessPointList']['accessPoints']
#
#         records_list_template = ','.join(['%s'] * len(ap_list))
#
#         columns="(ap_ip_addr,ap_group,ap_location,ap_model,ap_name,controller_desc,controller_ip,controller_model,controller_serial_num,controller_version,description,last_ap_reboot_reason,num_devices,uuid,voyance_url,created_at,last_updated)"
#
#         insert_query = "Insert into nya_ap_test {} values {}".format(columns,records_list_template)
#
#         cur.execute(insert_query,ap_list)
#
#         print(insert_query)
#         # psycopg2.extras.execute_values(
#         #     cursor, insert_query, data, template=None, page_size=100
#         # )
#         # cur.execute(insert_query,ap_list)
#         conn.commit()
#         cur.close()
#         conn.close()
#         print("record created!")
#     except(Exception, psycopg2.DatabaseError) as err:
#         print(err)
#     finally:
#         if conn is not None:
#             conn.close()
#
#             # ap_list = result['data']['accessPointList']['accessPoints']
#             # list_template = ','.join(['%s'] * 5)
#             # print(list_template)
#             # insert_query = 'insert into access_points (a, b, c, d, e) values {}'.format(list_template)
#             #
#             # print(insert_query)
#
# def nonecheck(ap):
#     if( type(ap["apRadios"]) is not str):
#         pass
#     if (ap["ipAddress"] is None):
#         ap["ipAddress"] = "None"
#     if (ap["apGroup"] is None):
#         ap["apGroup"] = "None"
#     if (ap["apLocation"] is None):
#         ap["apLocation"] = "None"
#     records = [ap["ipAddress"], ap["apGroup"], ap["apLocation"]]
#     join_str = ",".join(records)
#     print(">>"+join_str)
#     return join_str