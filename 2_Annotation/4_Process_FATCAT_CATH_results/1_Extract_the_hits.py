import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

filepath = 'Path_to_input'
file_name_list = os.listdir(filepath)
file_name_list_sorted = sorted(file_name_list, key = lambda x:int(x.split("_")[0]))
print(file_name_list_sorted)



def get_CATH_done(one):
    file_name = filepath + '/' + one
    data = pd.read_csv(file_name,skiprows=1,delimiter='\t',header=None,\
                       names = ["query","query length","hit","hit length","twist","iniLen","iniRmsd","optLen","optRms","chainRms","score","alnLen","gap","pval","AfpNum","Identity(%)","Similarity(%)"])

    print(data.shape) 
    print(data.index) 
    print(data.columns) 

    data2 = data.sort_values(by='score',ascending=False,ignore_index=True)
    print(data2[["hit",'score','pval','Identity(%)',"Similarity(%)"]].head(5))



    s_name1 = file_name.split("_")
    s_name2 = s_name1 [3] + "_" + s_name1 [4] + "_" + s_name1 [5]



    if len(data2) == 0:
        print("no data")
        CATH_dict[s_name2]='-'
    else:
        print("has data")
        names = data2["query"][0].split("_")
        name = names[1] + "_" + names[2] + "_" + names[3]
        Best_hit = data2["hit"][0]
        Best_P_value = data2["pval"][0]
        print(Best_P_value)

        P_value_dict[name] = Best_P_value
        if Best_P_value < 0.05:
            CATH_dict[name] = Best_hit

        else:
            CATH_dict[name] = '-'



CATH_dict = {}


P_value_dict = {}



for one in file_name_list_sorted:
    get_CATH_done(one)

print(CATH_dict)


import json
json_str = json.dumps(CATH_dict, indent=4)
with open("output/CATH_dict.json",'w') as json_file:
    json_file.write(json_str)

# for P_value
json_str = json.dumps(P_value_dict, indent=4)
with open("output/P_value_dict.json",'w') as json_file:
    json_file.write(json_str)
# for P_value


