import pandas as pd
from .custom_exceptions import ColumnValidationError


def string_operations(df: pd.DataFrame, config: dict) -> list:

    try:
        action_type = [*config.keys()][0]
        result = df.dtypes

        if action_type == "Column_padding":
            column_name = config["Column_padding"]["columns"]
            val = config["Column_padding"]["string_length"]
            string_length = int(val)
            character = config["Column_padding"]["character"]
            operator = config["Column_padding"]["operator"]
            for item in result.items():
                if item[0] == column_name:
                    if item[1] == "object":
                        df[column_name] = df[column_name].str.pad(
                            string_length, side=operator, fillchar=character
                        )
                        return [df]
                    else:
                        raise ColumnValidationError(" Can't handle numeric values")

        if action_type == "Column_merge_with_replace":
            column_name_1 = config["Column_merge_with_replace"]["column1"]
            column_name_2 = config["Column_merge_with_replace"]["column2"]
            column_name = config["Column_merge_with_replace"]["column_name_for_replace"]
            separator = config["Column_merge_with_replace"]["separator"]
            na_rep = config["Column_merge_with_replace"]["na_rep"]
            merge(
                df, result, column_name_1, column_name_2, column_name, separator, na_rep
            )
            return [df]

        if action_type == "Column_merge_with_new_column":
            column1 = config["Column_merge_with_new_column"]["column1"]
            column2 = config["Column_merge_with_new_column"]["column2"]
            column_name = config["Column_merge_with_new_column"]["new_column_name"]
            separator = config["Column_merge_with_new_column"]["separator"]
            na_rep = config["Column_merge_with_new_column"]["na_rep"]
            merge(df, result, column1, column2, column_name, separator, na_rep)
            return [df]
        if action_type == "substring":
            selected_column = config["substring"]["selected_column"]
            subsplit = config["substring"]["subsplit"]
            start_index = config["substring"]["start_index"]
            stop_index = config["substring"]["stop_index"]
            step = config["substring"]["step"]
            new_column = config["substring"]["new_column"]
            if new_column == "True":
                new_column_name = config["substring"]["new_column_name"]

            if subsplit == "substring":
                if new_column == "True":
                    df[new_column_name] = df[selected_column].str[
                        None
                        if start_index == ""
                        else int(start_index) : None
                        if stop_index == ""
                        else int(stop_index) : None
                        if step == ""
                        else int(step)
                    ]
                else:
                    df[selected_column] = df[selected_column].str[
                        None
                        if start_index == ""
                        else int(start_index) : None
                        if stop_index == ""
                        else int(stop_index) : None
                        if step == ""
                        else int(step)
                    ]
            return [df]

    except Exception as exec:
        raise exec


def merge(
    df: pd.DataFrame,
    result,
    column_name_1,
    column_name_2,
    column_name,
    separator,
    na_rep,
):
    for item in result.items():
        if item[0] == column_name_1:
            if item[1] == "object":
                for item in result.items():
                    if item[0] == column_name_2:
                        if item[1] == "object":
                            df[column_name] = df[column_name_1].str.cat(
                                df[column_name_2],
                                sep=separator,
                                na_rep=na_rep,
                                join="outer",
                            )
                            return [df]
                        else:
                            raise ColumnValidationError(" Can't handle numeric values")
