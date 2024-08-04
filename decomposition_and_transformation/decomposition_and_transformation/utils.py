import pandas as pd
import json
from .custom_exceptions import (
    CannotMapInputsException,
    ColumnNameNotMatchError,
)


def transformation(data_frame: pd.DataFrame, column_data: pd.DataFrame):
    try:
        column_names = []
        for item in column_data.iterrows():
            for item in item[1].iteritems():
                column_names.append(item[1])
        size = len(column_names)
        row_value = data_frame.count()
        for item in row_value.items():
            row_count = item[1]
        output_list = []
        for i in range(row_count):
            output_list.append([None] * size)

        index = 0
        for item in data_frame.iterrows():
            row = item[1]
            row_to_dict = json.loads(row.to_json())
            for i in row_to_dict:
                for j in row_to_dict.values():
                    dictionary = json.loads(j)
                    key_list = list(dictionary.keys())
                    key_list.sort()
                    keys = dictionary.keys()

                    for key in dictionary:
                        if type(dictionary[key]) is dict:
                            dictionary[key] = json.dumps(dictionary[key])
                    print(type(keys))
                    if (len(key_list) > len(column_names)) or (
                        len(key_list) < len(column_names)
                    ):
                        raise CannotMapInputsException("inputs Can't Map")

                    for k in keys:
                        flag = 0
                        for column_nam in column_names:
                            if column_nam == k:
                                flag = 1
                        if flag == 0:
                            raise ColumnNameNotMatchError(f" {k} not in inputed list")

                        key_index = column_names.index(k)

                        value = dictionary[k]
                        for j in column_names:
                            if j == k:
                                output_list[index][key_index] = value

            index = index + 1
        data_out = pd.DataFrame(output_list, columns=column_names)
        print(data_out)
        return data_out
    except Exception as exec:
        raise exec
