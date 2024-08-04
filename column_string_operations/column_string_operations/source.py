from .utils import string_operations
from .custom_exceptions import EmptyInputDataframeError


def process(input: dict) -> list:

    df = input["data"]
    print(f"Printing input dictionary: {input}")
    if df is None:
        raise EmptyInputDataframeError("The input dataframe is empty")
    print(f"Printing data: {df}")

    config = input["config"]
    print(f"Printing cong: {config}")
    Data_out = string_operations(df, config)
    print(f"Printing out: {Data_out}")
    return Data_out
