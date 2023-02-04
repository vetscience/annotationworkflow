import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
def load_dict(path):
    f = open(path,"r")

    return json.load(f)

CATH_dict  = load_dict("output/CATH_dict.json")
PDB_GO_dict = load_dict("input/PDB_GO/PDB_GO_dict.json")
CATH_GO={}
for one in CATH_dict.keys():
    print(one)
    if CATH_dict[one] == '-':
        CATH_GO[one] = '-'
    else:
        pdb_hit = CATH_dict[one][0:4]+"_"+CATH_dict[one][4]
        pdb_hit_2 = pdb_hit.upper()
        if pdb_hit_2 in PDB_GO_dict.keys():
            CATH_GO[one] = PDB_GO_dict[pdb_hit_2]
        else:
            CATH_GO[one] = '-'

print(CATH_GO)
CATH_GO_final = {}
f = open("input/Protein_list",'r')
for one in f.readlines():
    one = one.strip()
    if one in CATH_GO.keys():
        CATH_GO_final[one]=CATH_GO[one]
    else:
        CATH_GO_final[one]='-'




data3 = pd.DataFrame(CATH_GO_final, index=['GO'])
data3 = data3.T
data3.to_excel('output/CATH_GO_final.xlsx')

import json
json_str = json.dumps(CATH_GO_final, indent=4)
with open("output/CATH_GO_final.json",'w') as json_file:
    json_file.write(json_str)


