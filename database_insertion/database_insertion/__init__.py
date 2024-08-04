from .source import process

# import pandas as pd

# df = pd.read_csv("../Transaction.csv")

# input = {
#     "config": {
#         "hostname": "localhost",
#         "database": "Test_DB",
#         "user": "postgres",
#         "port": 5432,
#         "password": "manager123",
#     },
#     "data": df,
#     "operation_config": {
#         "Operation": {
#             "operations": "INSERT",
#             "column_name": "event_id,event_name,event_date,membership_number,activity_type,activity_date,activity_number,event_detail",
#             "table": "Transaction_Log",
#         },
#         #  "column_name": "ent_nevent_id, evame, event_date, membership_number, activity_type, activity_date, activity_number, event_detail",
#     },
# }
# # input = {
# #     "config": {
# #         "hostname": "10.246.28.37",
# #         "database": "test_kafka",
# #         "user": "oms_user",
# #         "port": 5432,
# #         "password":"oms_user",
# #     },
# #     "data": df,

# #     "operation_config": {
# #            "operation":"CREATE",
# #     #         "query": '''INSERT INTO public."Transaction_Log"(
# # 	# event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail)
# # 	# VALUES (%s,%s,%s,%s,%s,%s,%s,%s);''',
# #              "table": "TeacherS",
# #              "column_name": "id INT PRIMARY KEY NOT NULL, name TEXT NOT NULL, age INT NOT NULL",


# #     }
# # }
# # input = {
# #     "config": {
# #         "hostname": "localhost",
# #         "database": "Test_DB",
# #         "user": "postgres",
# #         "port": 5432,
# #         "password":"manager123",
# #     },
# #     "data": df,

# #     "operation_config": {
# #            "General_Query":{"general_query":'''INSERT INTO public."Transaction_Log"(event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail) VALUES ('35665cb8-3d5e-442b-b059-a9217606ddf1','T12','2017-07-28 03:11:35+05:30',10,'DEPOSIT','2017-07-28 03:11:35+05:30',10,'{"name":"Hary"}')''',


# #              "table": "Transaction_Log"}


# #     }
# # }
# df_out = process(input)
# print(df_out)
