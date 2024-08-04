from .custom_exceptions import (
    InputNotFoundException,
)
from .utils import transformation


def process(input: dict) -> list:

    data_frame = input["data"]
    print(f"Printing data: {data_frame}")
    if "data" not in input.keys() or input["data"] is None:
        raise InputNotFoundException("input is null or not found")
    column_data = input["column_data"]
    print(f"Printing 2nd input: {column_data}")
    if "column_data" not in input.keys() or input["column_data"] is None:
        raise InputNotFoundException("input is null or not found")
    data_out = transformation(data_frame, column_data)
    return [data_out]
