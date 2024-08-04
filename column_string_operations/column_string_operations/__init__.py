from .source import process

# import pandas as pd

# df = pd.DataFrame(
#     {
#         "BOOKING_DATE": [
#             "2015-07-31 22:00:00",
#             "2016-12-05 8:00:00",
#             "2014-08-10 12:00:00",
#             "2019-11-18 7:00:00",
#             "2014-07-19 20:00:00",
#             "2020-12-31 7:00:00",
#         ],
#         "FLIGHT_DATE": [
#             "2019-11-23 7:00:00",
#             "2019-12-18 18:00:00",
#             "2018-08-11 13:00:00",
#             "2019-11-30 19:00:00",
#             "2019-07-21 15:00:00",
#             "2021-01-07 18:00:00",
#         ],
#         "Category": ["Asian", "Hispanic", "Asian", "European", "Asian", "European"],
#         "cmpcod": ["IBS", "IBS", "IBS", "IBS", "IBS", "IBS"],
#         "x1": [
#             20.954659679060413,
#             18.31334025619164,
#             21.569927987912035,
#             19.515725455317845,
#             25.359630746494982,
#             22.359630746494982,
#         ],
#         "x2": [
#             28.403124298916406,
#             26.808441325755354,
#             29.993373813579744,
#             30.369820500803115,
#             25.60606661210394,
#             32.369820500803115,
#         ],
#     }
# )

# input = {
#     "data": df,
#     # "config": {
#     #     "Column_padding": {
#     #         "columns": "cmpcod",
#     #         "string_length": "15",
#     #         "operator": "both",
#     #         "character": "A",
#     #     }
#     # }
#     "config": {
#         "Column_merge_with_new_column": {
#             "column1": "Category",
#             "column2": "cmpcod",
#             "new_column_name": "Cat",
#             "separator": "_",
#             "na_rep": "?",
#         }
#     }
#     # 'config': {'rename': {'new_column': 'new', 'old_column': 'cmpcod'}}
#     #     "config": {
#     #         "substring": {
#     #             "selected_column": "Category",
#     #             "new_column": "True",
#     #             "new_column_name": "Cat",
#     #             "subsplit": "substring",
#     #             "start_index": "0",
#     #             "stop_index": "2",
#     #             "step": "1",
#     #         }
#     #     }
# }

# output = process(input)
