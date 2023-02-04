import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import itertools

data_3353_all = pd.read_csv("path_to_input",sep="\t", index_col=0)

data_split_into_3_3353_high_quality_GO = data_3353_all[["Eggnog_GOs","InterProScan_GO"\
    ,"CATH_GO","Deepfri_seq_GO","Deepfri_structure_GO"]]


InterPro_scan_and_Eggnog = []
CATH_plus = []
deep_plus = []
check = []

data_Eggnog_InterProScan = data_3353_all[~(data_3353_all["Eggnog_Description"] == "-") | \
                                  ~(data_3353_all["Eggnog_EC"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_ko"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_Pathway"] == "-") | \
                                  ~(data_3353_all["Eggnog_Pfam"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_Module"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_Reaction"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_rclass"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_TC"] == "-") | \
                                  ~(data_3353_all["Eggnog_BRITE"] == "-") | \
                                  ~(data_3353_all["Eggnog_CAZy"] == "-") | \
                                  ~(data_3353_all["Eggnog_BiGG_Reaction"] == "-") | \
                                  ~(data_3353_all["InterProScan_InterPro_hit"] == "-") | \
                                  ~(data_3353_all["InterProScan_Pathway"] == "-") | \
                                  ~(data_3353_all["Eggnog_GOs"] == "-") | \
                                  ~(data_3353_all["InterProScan_GO"] == "-") | \
                                  ~(data_3353_all["InterProScan_GO"] == "-") ]

num_eggnog_interproscan = len(data_Eggnog_InterProScan)
print(num_eggnog_interproscan)

data_Eggnog_InterProScan_FATCAT_CATH = data_3353_all[~(data_3353_all["Eggnog_Description"] == "-") | \
                                  ~(data_3353_all["Eggnog_EC"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_ko"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_Pathway"] == "-") | \
                                  ~(data_3353_all["Eggnog_Pfam"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_Module"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_Reaction"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_rclass"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_TC"] == "-") | \
                                  ~(data_3353_all["Eggnog_BRITE"] == "-") | \
                                  ~(data_3353_all["Eggnog_CAZy"] == "-") | \
                                  ~(data_3353_all["Eggnog_BiGG_Reaction"] == "-") | \
                                  ~(data_3353_all["InterProScan_InterPro_hit"] == "-") | \
                                  ~(data_3353_all["InterProScan_Pathway"] == "-") | \
                                  ~(data_3353_all["Eggnog_GOs"] == "-") | \
                                  ~(data_3353_all["InterProScan_GO"] == "-") | \
                                  ~(data_3353_all["InterProScan_GO"] == "-") | \
                                  ~(data_3353_all["CATH_hit_structure"] == "-") | \
                                  ~(data_3353_all["CATH_GO"] == "-")]

num_Eggnog_InterProScan_FATCAT_CATH = len(data_Eggnog_InterProScan_FATCAT_CATH)
print(num_Eggnog_InterProScan_FATCAT_CATH)


data_Eggnog_InterProScan_FATCAT_CATH_DeepFRI = data_3353_all[~(data_3353_all["Eggnog_Description"] == "-") | \
                                  ~(data_3353_all["Eggnog_EC"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_ko"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_Pathway"] == "-") | \
                                  ~(data_3353_all["Eggnog_Pfam"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_Module"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_Reaction"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_rclass"] == "-") | \
                                  ~(data_3353_all["Eggnog_KEGG_TC"] == "-") | \
                                  ~(data_3353_all["Eggnog_BRITE"] == "-") | \
                                  ~(data_3353_all["Eggnog_CAZy"] == "-") | \
                                  ~(data_3353_all["Eggnog_BiGG_Reaction"] == "-") | \
                                  ~(data_3353_all["InterProScan_InterPro_hit"] == "-") | \
                                  ~(data_3353_all["InterProScan_Pathway"] == "-") | \
                                  ~(data_3353_all["Eggnog_GOs"] == "-") | \
                                  ~(data_3353_all["InterProScan_GO"] == "-") | \
                                  ~(data_3353_all["InterProScan_GO"] == "-") | \
                                  ~(data_3353_all["CATH_hit_structure"] == "-") | \
                                  ~(data_3353_all["CATH_GO"] == "-") | \
                                  ~(data_3353_all["DeeoFri_seq_EC_value"] == "-") | \
                                  ~(data_3353_all["DeeoFri_structure_EC_value"] == "-") | \
                                  ~(data_3353_all["combined_GO"] == "-") ]

num_Eggnog_InterProScan_FATCAT_CATH_DeepFRI = len(data_Eggnog_InterProScan_FATCAT_CATH_DeepFRI)
print(num_Eggnog_InterProScan_FATCAT_CATH_DeepFRI)

num_dark_matter = 3353 - num_Eggnog_InterProScan_FATCAT_CATH_DeepFRI


fig1, ax1 = plt.subplots()
y = np.array([num_eggnog_interproscan, num_Eggnog_InterProScan_FATCAT_CATH - num_eggnog_interproscan, num_Eggnog_InterProScan_FATCAT_CATH_DeepFRI - num_Eggnog_InterProScan_FATCAT_CATH, num_dark_matter])   #
ax1.pie(y,
        labels=['Eggnog and InterProScan','FATCAT-CATH','DeepFRI','Dark_matter'], 
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 
        explode=(0, 0.2, 0, 0), 
        autopct='%.2f%%', 
       )

plt.show()
fig1.savefig("output/Fig_1_pie_all_hit_without_SP_refined_3353.png")




#
data_split_into_3_3395_high_quality_GO = data_split_into_3_3395_high_quality_GO


data_GO_eggnong_interproscan = data_split_into_3_3395_high_quality_GO[~(data_split_into_3_3395_high_quality_GO["Eggnog_GOs"] == "-") | \
                                  ~(data_split_into_3_3395_high_quality_GO["InterProScan_GO"] == "-")]


num_eggnog_interproscan_GO = len(data_GO_eggnong_interproscan)
print(num_eggnog_interproscan_GO)

data_GO_eggnong_interproscan_CATH = data_split_into_3_3395_high_quality_GO[~(data_split_into_3_3395_high_quality_GO["Eggnog_GOs"] == "-") | \
                                     ~(data_split_into_3_3395_high_quality_GO["InterProScan_GO"] == "-") | \
                                     ~(data_split_into_3_3395_high_quality_GO["CATH_GO"] == "-")]


num_eggnog_interproscan_GO_cath = len(data_GO_eggnong_interproscan_CATH)
print(num_eggnog_interproscan_GO_cath)


data_GO_eggnong_interproscan_CATH_deep = data_split_into_3_3395_high_quality_GO[~(data_split_into_3_3395_high_quality_GO["Eggnog_GOs"] == "-") | \
                                     ~(data_split_into_3_3395_high_quality_GO["InterProScan_GO"] == "-") | \
                                     ~(data_split_into_3_3395_high_quality_GO["CATH_GO"] == "-") | \
                                     ~(data_split_into_3_3395_high_quality_GO["Deepfri_seq_GO"] == "-") | \
                                     ~(data_split_into_3_3395_high_quality_GO["Deepfri_structure_GO"] == "-") ]


num_eggnog_interproscan_GO_cath_deep = len(data_GO_eggnong_interproscan_CATH_deep)
print(num_eggnog_interproscan_GO_cath_deep)

num_dark_matter_go = 3353 - num_eggnog_interproscan_GO_cath_deep


fig1, ax1 = plt.subplots()
y = np.array([num_eggnog_interproscan_GO, num_eggnog_interproscan_GO_cath - num_eggnog_interproscan_GO, num_eggnog_interproscan_GO_cath_deep - num_eggnog_interproscan_GO_cath, num_dark_matter_go])   #
ax1.pie(y,
        labels=['Eggnog and InterProScan_GO','FATCAT-CATH_GO','DeepFRI_GO','Dark_matter_GO'], 
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"],
        explode=(0, 0.2, 0, 0),
        autopct='%.2f%%', 
       )

plt.show()
fig1.savefig("path_to_output")