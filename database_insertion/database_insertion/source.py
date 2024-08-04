from typing import Dict
from .utils import get_operations
from .custom_exceptions import EmptyInputDataframeError


def process(input: Dict):
    credentials = input["config"]
    operations = input["operation_config"]
    DataFrame = input["data"]
    print(DataFrame)
    if DataFrame is None:
        raise EmptyInputDataframeError("The input dataframe is empty")
    data_out = get_operations(operations, credentials, DataFrame)
    print(data_out)
    return [data_out]
