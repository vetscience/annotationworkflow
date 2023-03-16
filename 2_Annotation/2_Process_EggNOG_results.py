import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("Path_to_input_file",sep="\t")
print(data.columns)
print(data.shape)
print(data.index)
print(data.head(5))
index_list = []
for row in data.itertuples(index=False, name='eggnog'):
    name1 = row.query
    name2 = row.query.split("@")[1].replace("-","_")[:19]
    index_list.append(name2)

data.index = index_list

print(data.head(5))

f = open("input_raw/Protein_list",'r')

All_protein_name_list = []
Eggnog_OG_hit_list = []
Eggnog_Description_list = []
Eggnog_GOs_list = []
Eggnog_EC_list = []
Eggnog_KEGG_ko_list = []
Eggnog_Pfam_list = []


Eggnog_KEGG_Module_list  = []
Eggnog_KEGG_Reaction_list  = []
Eggnog_KEGG_rclass_list  = []
Eggnog_BRITE_list  = []
Eggnog_CAZy_list  = []
Eggnog_BiGG_Reaction_list  = []


for one in f.readlines():
    one = one.strip()
    if one in index_list:
        Eggnog_OG_hit = data.at[one,"eggNOG_OGs"]
        Eggnog_Description = data.at[one,"Description"]
        Eggnog_GOs = data.at[one, "GOs"]
        Eggnog_EC = data.at[one, "EC"]
        Eggnog_KEGG_ko = data.at[one, "KEGG_ko"]
        Eggnog_Pfam = data.at[one, "PFAMs"]


        Eggnog_KEGG_Module = data.at[one, "KEGG_Module"]
        Eggnog_KEGG_Reaction = data.at[one, "KEGG_Reaction"]
        Eggnog_KEGG_rclass = data.at[one, "KEGG_rclass"]
        Eggnog_BRITE = data.at[one, "BRITE"]
        Eggnog_CAZy = data.at[one, "CAZy"]
        Eggnog_BiGG_Reaction = data.at[one, "BiGG_Reaction"]

    else:
        Eggnog_OG_hit = '-'
        Eggnog_Description = '-'
        Eggnog_GOs = '-'
        Eggnog_EC = '-'
        Eggnog_KEGG_ko = '-'
        Eggnog_Pfam = '-'


        Eggnog_KEGG_Module = '-'
        Eggnog_KEGG_Reaction = '-'
        Eggnog_KEGG_rclass = '-'
        Eggnog_BRITE = '-'
        Eggnog_CAZy = '-'
        Eggnog_BiGG_Reaction = '-'


    All_protein_name_list.append(one)
    Eggnog_OG_hit_list.append(Eggnog_OG_hit)
    Eggnog_Description_list.append(Eggnog_Description)
    Eggnog_GOs_list.append(Eggnog_GOs)
    Eggnog_EC_list.append(Eggnog_EC)
    Eggnog_KEGG_ko_list.append(Eggnog_KEGG_ko)
    Eggnog_Pfam_list.append(Eggnog_Pfam)

    
    Eggnog_KEGG_Module_list.append(Eggnog_KEGG_Module)
    Eggnog_KEGG_Reaction_list.append(Eggnog_KEGG_Reaction)
    Eggnog_KEGG_rclass_list.append(Eggnog_KEGG_rclass)
    Eggnog_BRITE_list.append(Eggnog_BRITE)
    Eggnog_CAZy_list.append(Eggnog_CAZy)
    Eggnog_BiGG_Reaction_list.append(Eggnog_BiGG_Reaction)



data6 = pd.DataFrame({
    "Eggnog_OG_hit":Eggnog_OG_hit_list,
    "Eggnog_Description":Eggnog_Description_list,
    "Eggnog_GOs": Eggnog_GOs_list,
    "Eggnog_EC": Eggnog_EC_list,
    "Eggnog_KEGG_ko": Eggnog_KEGG_ko_list,
    "Eggnog_Pfam": Eggnog_Pfam_list,

    
    "Eggnog_KEGG_Module": Eggnog_KEGG_Module_list,
    "Eggnog_KEGG_Reaction": Eggnog_KEGG_Reaction_list,
    "Eggnog_KEGG_rclass": Eggnog_KEGG_rclass_list,
    "Eggnog_BRITE": Eggnog_BRITE_list,
    "Eggnog_CAZy": Eggnog_CAZy_list,
    "Eggnog_BiGG_Reaction": Eggnog_BiGG_Reaction_list,

})


data6.index = All_protein_name_list
print(data6.head(55))

data6.to_csv('Path_to_output_file',sep='\t')
