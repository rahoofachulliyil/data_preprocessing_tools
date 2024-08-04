import pandas as pd
from numpy import nan
from .custom_exceptions import EmptyInputDataframeError

def process(input: dict) -> list:

    df = input["data"]
    column_mappping_info=input["column_map_info"]
    if df is None:
        raise EmptyInputDataframeError("The input dataframe is empty")
    if column_mappping_info is None:
        raise EmptyInputDataframeError("The input dataframe is empty")
    separator=input ["column_config"]["separator"]
    null=input ["column_config"]["na_rep"]
    column_count=len(column_mappping_info.axes[1])
    column_mer=column_mappping_info.iloc[:,0:column_count-1]
    print(column_mer)
    new_column_name=column_mappping_info.iloc[:,-1:]
    print(new_column_name)
    row_count=column_mer.shape[0]
    column_name=new_column_name.iloc[:,-1:].values.tolist()
    size=len(column_name)
    print(column_name)
    print(row_count)
    g = globals()
    
    for i in range(1,row_count+1):
        g['column{0}'.format(i)]= f"column{i}"
        
    for i in range(row_count):
         list11=column_mer.iloc[i, :].values.tolist()
         list1 = [item for item in list11 if not(pd.isnull(item)) == True]
         print(list1)
         df[ g['column{0}'.format(i+1)]] = df[list1[0]].str.cat(df[list1[1]],sep=separator,na_rep=null,join='outer')
         for j in range(2,len(list1)):
              df[ g['column{0}'.format(i+1)]] = df[ g['column{0}'.format(i+1)]].str.cat(df[list1[j]],sep=separator,na_rep=null,join='outer')
      
    print(df)
    drop_list=[]
    for i in range(row_count):
        list11=column_mer.iloc[i, :].values.tolist()
        list1 = [item for item in list11 if not(pd.isnull(item)) == True]
        print(list1)
        for i in range(0,len(list1)):
            drop_list.append(list1[i])
    print(drop_list)
    new_df= df.drop(drop_list,axis=1)
    print(list(new_df.columns))
    for i in range(0,size):
     if column_name[i][0]!=None:
        #  df[f"column{i+1}"]=column_name[i][0]
         new_df.rename(columns = {f"column{i+1}":column_name[i][0]}, inplace = True)
     else:
         new_df.rename(columns = {f"column{i+1}":f"column{i+1}"}, inplace = True)
    print(list(new_df.columns))
    print(new_df)
    return [new_df]