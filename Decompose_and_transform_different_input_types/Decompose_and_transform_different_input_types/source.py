import pandas as pd
import json


from .custom_exceptions import (
    InputNotFoundException,
    CannotMapInputsException,
    ValueError,
)


def process(input: dict) -> list:

    data_frame = input["data"]
    print(f"Printing data: {data_frame}")
    if "data" not in input.keys() or input["data"] is None:
        raise InputNotFoundException("input is null or not found")
    column_data= input["column_data"]
    print(f"Printing 2nd input: {column_data}")
   
    if "column_data" not in input.keys() or input["column_data"] is None:
        raise InputNotFoundException("input is null or not found")
    cols = len(column_data.axes[1])
    print(f"Printing columns: {cols}")
    columns=[]
    # for i in range(0,cols):
    g = globals()
    for i in range(0, cols):
      g['depth_{0}'.format(i)] = []
      print(f"depth_{1}")
      g['index{0}'.format(i)]=0


    try:

        # for i in range(1,(cols+1)):
        i=0   
        for column in column_data.columns:
               columns.append(column_data[column].tolist())
        print (f"column_name{columns}")
        
           
            
        # column_names1= []
        # for item in column_data.():
        #     for item in item[1].iteritems():
        #         column_names1.append(item[1])
        size1 = len(columns[0])
        # print(f"Printing size: {size1}")
        # column_names2= []
        # for item in column_data2.iterrows():
        #     for item in item[1].iteritems():
        #         column_names2.append(item[1])
        # size2 = len(column_names2)
        # row_value = data_frame.count()
        # for item in row_value.items():
        #     row_count = item[1]
        # output_list1 = []
        # output_list2 = []

        # for i in range(row_count):
        #     output_list.append([None] * size)
        # print(f"output list:{output_list}")

       
        index2=0
        for item in data_frame.iterrows():
            print(f"Printing row: {item}")
            row = item[1]
            print(f"Printing row[1]: {row}")
            row_to_dict = json.loads(row.to_json())
            print(f"Printing row to dict: {row_to_dict}")
            for m in row_to_dict:
                print(f"Printing key: {m}")
                for j in row_to_dict.values():
                    print(f"printinf type{type(j)}")
                    dictionary = json.loads(j)
                    print(f"Printing dict: {dictionary}")

                    key_list = list(dictionary.keys())
                    for i in range(cols):
                    
                     if key_list==columns[i]:
                         g['depth_{0}'.format(i)].append([None]*size1)
                         print(['depth_{0}'.format(i)])
                         keys = dictionary.keys()

                         for key in dictionary:
                          if type(dictionary[key]) is dict:
                            dictionary[key] = json.dumps(dictionary[key])

                         print(f"Printing dict afrer chnage: {dictionary}")

                         print(type(keys))
                         if (len(key_list) > len(columns[i])) or (
                        len(key_list) < len(columns[i])
                    ):
                          raise CannotMapInputsException("inputs Can't Map")
                         for k in keys:
                           try:
                            key_index = columns[i].index(k)
                            
                           except ValueError:
                            raise ValueError(f" {k}not in list")
                           value = dictionary[k]
                           for j in columns[i]:
                            if j == k:
                                print(g['index{0}'.format(i)])
                                g['depth_{0}'.format(i)] [g['index{0}'.format(i)]][key_index] = value
                         print(g['depth_{0}'.format(i)])
                         print( g['index{0}'.format(i)])
                         g['index{0}'.format(i)]= g['index{0}'.format(i)]+1
                    # if key_list==column_names2: 
                    #      output_list2.append([None] * size2)                   
                   
                    #      keys = dictionary.keys()

                    #      for key in dictionary:
                    #        if type(dictionary[key]) is dict:
                    #         dictionary[key] = json.dumps(dictionary[key])

                    #      print(f"Printing dict afrer chnage: {dictionary}")

                    #      print(type(keys))
                    #      if (len(key_list) > len(column_names2)) or (
                    #     len(key_list) < len(column_names2)
                    # ):
                    #       raise CannotMapInputsException("inputs Can't Map")
                    #      for k in keys:
                    #        try:
                    #         key_index = column_names2.index(k)
                    #        except ValueError:
                    #         raise ValueError(f" {k}not in list")
                    #        value = dictionary[k]
                    #        for j in column_names2:
                    #         if j == k:
                    #             output_list2[index2][key_index] = value

                    #      index2 = index2 + 1
        print(f"printing final list1111:{depth_0}")
        print(f"printing final list222:{depth_1}")
        print(f"printing final list333:{depth_2}")
        
        # print(f"printing final list:{output_list2}")
        for l in range(0,cols):
         g['data_out{0}'.format(l)] = pd.DataFrame(g['depth_{0}'.format(l)], columns=columns[l])
        #  data_out1 = pd.DataFrame(g['depth_{0}'.format(i)], columns=columns[l])
        # print(data_out1)
        #  data_out2= pd.DataFrame(output_list2, columns=column_names2)
         print(g['data_out{0}'.format(l)])
        data_out=data_out0
        for l in range(1,cols):
          data_out=pd.concat([data_out,g['data_out{0}'.format(l)]], axis=0, ignore_index=True)
        print(data_out)
        return[data_out]
        for item in data_out.items():
             print(item)
        
        # return [data_out]
    except Exception as exec:
        raise exec
