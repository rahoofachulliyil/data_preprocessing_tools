from .custom_exceptions import EmptyInputDataframeError

def process(input: dict) -> list:
 try:
    df = input["data"]
    if df is None:
        raise EmptyInputDataframeError("The input dataframe is empty")
    column_mappping_info=input["column_map_info"]
    if column_mappping_info  is None:
        raise EmptyInputDataframeError("The input dataframe is empty")
    row_count=column_mappping_info.shape[0]
    print(row_count)
    dataframe_output = df
    for i in range(0,row_count):
        list11=column_mappping_info.iloc[i, :].values.tolist()
        print(list11)
        
        dataframe_output.rename(
                columns={list11[0]: list11[1]}, inplace=True
            )
    print(dataframe_output)
    return [dataframe_output]
 except Exception as exec:
         raise exec
