import pytest
import pandas as pd
from source import process
from custom_exceptions import (
   EmptyInputDataframeError
)
from pandas._testing import assert_frame_equal

@pytest.fixture
def df():

 return (pd.read_csv("Tranform_output.csv"))
@pytest.fixture
def column_map_info():
    return(pd.read_csv("Column_merge1.csv"))
def test_process_input_df_is_empty(column_map_info):
    df_test = None
    input = {
    "data": df_test,
    #'config': {'column1': 'cmpcod', 'column2': 'prgcod'}, 'column_config': {'new_column': {'new_column_name': 'F'}}}
    "column_map_info": column_map_info,
    "column_config": 
       {"separator": "_","na_rep": "?",
            
        
    }

    }
    with pytest.raises(EmptyInputDataframeError):
        df_in = process(input)
def test_process_input_df2_is_empty(df):
    df_test = None
    input = {
    "data": df,
    #'config': {'column1': 'cmpcod', 'column2': 'prgcod'}, 'column_config': {'new_column': {'new_column_name': 'F'}}}
    "column_map_info": df_test,
    "column_config": 
       {"separator": "_","na_rep": "?",
            
        
    }

    }
    with pytest.raises(EmptyInputDataframeError):
        df_in = process(input)
