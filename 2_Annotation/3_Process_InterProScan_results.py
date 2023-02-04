import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

def load_dict(path):
    f = open(path,"r")

    return json.load(f)

InterProScan_GO  = load_dict("output/pandas_interpro_GO_dict")
InterProScan_InterPro_hit = load_dict("output/pandas_interpro_InterPro_dict")
InterProScan_Pathway = load_dict("output/pandas_interpro_pathway_dict")

InterProScan_name_list = []
InterProScan_GO_list = []
InterProScan_InterPro_hit_list = []
InterProScan_Pathway_list = []

f = open("Path_to_input",'r')
for one in f.readlines():
    one = one.strip()
    if one in InterProScan_GO.keys():
        InterProScan_GO_item = InterProScan_GO[one]
    else:
        InterProScan_GO_item = '-'
    if one in InterProScan_InterPro_hit.keys():
        InterProScan_InterPro_hit_item = InterProScan_InterPro_hit[one]
    else:
        InterProScan_InterPro_hit_item = '-'
    if one in InterProScan_Pathway.keys():
        InterProScan_Pathway_item = InterProScan_Pathway[one]
    else:
        InterProScan_Pathway_item = '-'

    InterProScan_name_list.append(one)
    InterProScan_GO_list.append(InterProScan_GO_item)
    InterProScan_InterPro_hit_list.append(InterProScan_InterPro_hit_item)
    InterProScan_Pathway_list.append(InterProScan_Pathway_item)

data6 = pd.DataFrame({
    "InterProScan_GO":InterProScan_GO_list,
    "InterProScan_InterPro_hit": InterProScan_InterPro_hit_list,
    "InterProScan_Pathway": InterProScan_Pathway_list
})
data6.index = InterProScan_name_list

data6.to_csv('Path_to_output',sep='\t')