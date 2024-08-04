# Column String Operations

## Description

The purpose of this tool is to perform string operations on dataframe.Merging of two columns can be performed only by outer joins. Padding operation can be applied to column values.

## Inputs

data : dataframe -> input dataset<br/>
config : Dict -> includes the options to configure the 'Action Type' as 'Column_padding' with attibutes 'Column Name' ,'String_length' ,'operator' and 'character' or 'Column_merge_with replace' with attibutes 'column_1' ,'column2','column_name for replace,'separator' and 'na_rep or Column_merge_with_new_column' with attibutes 'column_1' ,'column2','new_column_name,'separator' and 'na_rep ,

## Outputs

data : dataframe -> output dataset
