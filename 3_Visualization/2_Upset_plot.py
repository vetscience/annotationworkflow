import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from venn import venn
from upsetplot import plot, from_indicators, from_contents

plt.style.use('ggplot') 
font1 = {'family':'Arial', 'weight':'normal', 'size':14, 'color': 'black'}
font2 = {'family':'Arial', 'weight':'normal', 'size':20, 'color': 'black'}
colour1 = ['#F6B93B','#F6B93B','#E55039', '#4A69BD', '#60A3BC', '#60A3BC','#60A3BC','#60A3BC','#60A3BC','#60A3BC','#60A3BC','#78E08F', '#BBEA99']
colour2 = {'#2D445F', '#3F4D50', '#494263', '#2279B6', '#7B9067', '#B56B62'}
colour3 = {'#F53B57', '#3C40C6', '#3C40C6', '#00D8D6', '#05C46B', '#C9C9C9'}
cmaps = ['#F6B93B', '#E55039','#4A69BD', '#60A3BC', '#BBEA99']

data_Protein_all_raw = pd.read_csv("path_to_input",sep="\t", index_col=0)

def add_name_in_list(dataframe,datalist):
    for index, row in dataframe.iterrows():
        datalist.append(index)

#for Eggnog
Eggnog_all_list = []
Eggnog_GO_list = []

data_Eggnog_all = data_Protein_all_raw[~(data_Protein_all_raw["Eggnog_Description"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_EC"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_KEGG_ko"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_KEGG_Pathway"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_Pfam"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_KEGG_Module"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_KEGG_Reaction"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_KEGG_rclass"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_KEGG_TC"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_BRITE"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_CAZy"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_BiGG_Reaction"] == "-") | \
                                  ~(data_Protein_all_raw["Eggnog_GOs"] == "-") ]

add_name_in_list(data_Eggnog_all,Eggnog_all_list)

data_Eggnog_GO = data_Protein_all_raw[~(data_Protein_all_raw["Eggnog_GOs"] == "-") ]
add_name_in_list(data_Eggnog_GO,Eggnog_GO_list)

#for InterProScan
InterProScan_all_list = []
InterProScan_GO_list = []

data_InterProScan_all = data_Protein_all_raw[~(data_Protein_all_raw["InterProScan_InterPro_hit"] == "-") | \
                                  ~(data_Protein_all_raw["InterProScan_Pathway"] == "-") | \
                                  ~(data_Protein_all_raw["InterProScan_GO"] == "-") ]

add_name_in_list(data_InterProScan_all,InterProScan_all_list)

data_InterProScan_GO = data_Protein_all_raw[~(data_Protein_all_raw["InterProScan_GO"] == "-") ]
add_name_in_list(data_InterProScan_GO,InterProScan_GO_list)

#for FATCAT_CATH
FATCAT_CATH_all_list = []
FATCAT_CATH_GO_list = []

data_FATCAT_CATH_all = data_Protein_all_raw[~(data_Protein_all_raw["CATH_hit_structure"] == "-") | \
                                        ~(data_Protein_all_raw["CATH_GO"] == "-") ]

add_name_in_list(data_FATCAT_CATH_all,FATCAT_CATH_all_list)

data_FATCAT_CATH_GO = data_Protein_all_raw[~(data_Protein_all_raw["CATH_GO"] == "-") ]
add_name_in_list(data_FATCAT_CATH_GO,FATCAT_CATH_GO_list)

#for DeepFRI_seq
DeepFRI_seq_all_list = []
DeepFRI_seq_GO_list = []

data_DeepFRI_seq_all = data_Protein_all_raw[~(data_Protein_all_raw["DeeoFri_seq_EC_value"] == "-") | \
                                        ~(data_Protein_all_raw["Deepfri_seq_GO"] == "-") ]

add_name_in_list(data_DeepFRI_seq_all,DeepFRI_seq_all_list)

data_DeepFRI_seq_GO = data_Protein_all_raw[~(data_Protein_all_raw["Deepfri_seq_GO"] == "-") ]
add_name_in_list(data_DeepFRI_seq_GO,DeepFRI_seq_GO_list)

#for DeepFRI_structure
DeepFRI_structure_all_list = []
DeepFRI_structure_GO_list = []

data_DeepFRI_structure_all = data_Protein_all_raw[~(data_Protein_all_raw["DeeoFri_structure_EC_value"] == "-") | \
                                        ~(data_Protein_all_raw["Deepfri_structure_GO"] == "-") ]

add_name_in_list(data_DeepFRI_structure_all,DeepFRI_structure_all_list)

data_DeepFRI_structure_GO = data_Protein_all_raw[~(data_Protein_all_raw["Deepfri_structure_GO"] == "-") ]
add_name_in_list(data_DeepFRI_structure_GO,DeepFRI_structure_GO_list)


All_5_dict_all = {
                  "DeepFRI-str combined annotation":DeepFRI_structure_all_list,
                  "DeepFRI-seq combined annotation":DeepFRI_seq_all_list,
                  "FATCAT-CATH combined annotation":FATCAT_CATH_all_list,
                  "InterProScan combined annotation":InterProScan_all_list,
                  "Eggnog combined annotation":Eggnog_all_list
}

#Upplot_all
upset_plot = from_contents(All_5_dict_all)

fig = plt.figure(figsize=(20,18))
plot(upset_plot, fig=fig, sort_by="cardinality", subset_size='count',min_degree=1, max_degree=6,show_counts='%d',facecolor='#78E08F',element_size=32, sort_categories_by=None)
#plt.suptitle('Matched annotation intersection', fontsize=14)
plt.savefig("output/fig_2_Upsetplot_3353_without_SP_all_refined.png", dpi=500)

All_5_dict_GO = {
                  "DeepFRI-str GO annotation":DeepFRI_structure_GO_list,
                  "DeepFRI-seq GO annotation": DeepFRI_seq_GO_list,
                  "FATCAT-CATH GO annotation": FATCAT_CATH_GO_list,
                  "InterProScan GO annotation": InterProScan_GO_list,
                  "Eggnog GO annotation":Eggnog_GO_list
}

#Upplot_GO
upset_plot = from_contents(All_5_dict_GO )

fig = plt.figure(figsize=(20,18))
plot(upset_plot, fig=fig, sort_by="cardinality", subset_size='count',min_degree=1, max_degree=6,show_counts='%d',facecolor='#60A3BC',element_size=32,sort_categories_by=None)
plt.savefig("output/fig_3_Upsetplot_3353_without_SP_GO_refined.png", dpi=500)
