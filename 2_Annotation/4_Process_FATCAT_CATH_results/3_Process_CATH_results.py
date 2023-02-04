import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

def load_dict(path):
    f = open(path,"r")

    return json.load(f)

CATH_hit = load_dict("output/CATH_dict.json")
CATH_GO  = load_dict("output/CATH_GO_final.json")

#For_Pvalue
CATH_P_value = load_dict("output/P_value_dict.json")

CATH_hit_list = []
CATH_GO_list = []
CATH_name_list = []

#For_Pvalue
CATH_P_value_list = []

f = open("input/Protein_list",'r')
for one in f.readlines():
    one = one.strip()
    if one in CATH_hit.keys():
        CATH_hit_item = CATH_hit[one]
    else:
        CATH_hit_item = '-'
    if one in CATH_GO.keys():
        CATH_GO_item = CATH_GO[one]
    else:
        CATH_GO_item = '-'

    if one in CATH_P_value.keys():
        CATH_P_value_item = CATH_P_value[one]
    else:
        CATH_P_value_item = '-'

    CATH_hit_list.append(CATH_hit_item)
    CATH_GO_list.append(CATH_GO_item)
    CATH_name_list.append(one)

    CATH_P_value_list.append(CATH_P_value_item)


data6 = pd.DataFrame({
    "CATH_hit_structure":CATH_hit_list,
    "CATH_GO": CATH_GO_list,
    "CATH_Pvalue": CATH_P_value_list,
})
data6.index = CATH_name_list

data6.to_csv('Path_to_output',sep='\t')