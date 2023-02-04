import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from venn import venn
from upsetplot import plot, from_indicators, from_contents

plt.style.use('ggplot') # choose style
font1 = {'family':'Arial', 'weight':'normal', 'size':14, 'color': 'black'}
font2 = {'family':'Arial', 'weight':'normal', 'size':20, 'color': 'black'}
colour1 = ['#F6B93B','#F6B93B','#E55039', '#4A69BD', '#60A3BC', '#60A3BC','#60A3BC','#60A3BC','#60A3BC','#60A3BC','#60A3BC','#78E08F', '#BBEA99']
colour2 = {'#2D445F', '#3F4D50', '#494263', '#2279B6', '#7B9067', '#B56B62'}
colour3 = {'#F53B57', '#3C40C6', '#3C40C6', '#00D8D6', '#05C46B', '#C9C9C9'}
cmaps = ['#F6B93B', '#E55039','#4A69BD', '#60A3BC', '#BBEA99']

data_protein_all_raw = pd.read_csv("Path_to_input",sep="\t", index_col=0)

def add_name_in_list(dataframe,datalist):
    for index, row in dataframe.iterrows():
        datalist.append(index)


#for Eggnog
Eggnog_all_list = []

data_Eggnog_all = data_protein_all_raw[~(data_protein_all_raw["Eggnog_Description"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_EC"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_KEGG_ko"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_KEGG_Pathway"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_Pfam"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_KEGG_Module"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_KEGG_Reaction"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_KEGG_rclass"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_KEGG_TC"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_BRITE"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_CAZy"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_BiGG_Reaction"] == "-") | \
                                  ~(data_protein_all_raw["Eggnog_GOs"] == "-") ]

add_name_in_list(data_Eggnog_all,Eggnog_all_list)

#for InterProScan
InterProScan_all_list = []

data_InterProScan_all = data_protein_all_raw[~(data_protein_all_raw["InterProScan_InterPro_hit"] == "-") | \
                                          ~(data_protein_all_raw["InterProScan_Pathway"] == "-") | \
                                          ~(data_protein_all_raw["InterProScan_GO"] == "-") ]

add_name_in_list(data_InterProScan_all,InterProScan_all_list)


#for FATCAT_CATH
FATCAT_CATH_all_list = []

data_FATCAT_CATH_all = data_protein_all_raw[~(data_protein_all_raw["CATH_hit_structure"] == "-") | \
                                         ~(data_protein_all_raw["CATH_GO"] == "-") ]

add_name_in_list(data_FATCAT_CATH_all,FATCAT_CATH_all_list)

#for DeepFRI_seq
DeepFRI_seq_all_list = []

data_DeepFRI_seq_all = data_protein_all_raw[~(data_protein_all_raw["DeeoFri_seq_EC_value"] == "-") | \
                                        ~(data_protein_all_raw["Deepfri_seq_GO"] == "-") ]

add_name_in_list(data_DeepFRI_seq_all,DeepFRI_seq_all_list)

#for DeepFRI_structure
DeepFRI_structure_all_list = []

data_DeepFRI_structure_all = data_protein_all_raw[~(data_protein_all_raw["DeeoFri_structure_EC_value"] == "-") | \
                                        ~(data_protein_all_raw["Deepfri_structure_GO"] == "-") ]

add_name_in_list(data_DeepFRI_structure_all,DeepFRI_structure_all_list)



# Venn begin

Eggnog_interproscan_fatcat_cath ={"Eggnog":set(Eggnog_all_list),
                                  "InterProScan":set(InterProScan_all_list),
                                  "FATCAT-CATH":set(FATCAT_CATH_all_list)
                                  }

# Venn - Eggnog-interproscan-fatcat-cath
fig1, ax1 = plt.subplots(figsize=(11.69,8.27), layout='constrained')  
ax1 = venn(Eggnog_interproscan_fatcat_cath, cmap=cmaps, fontsize=10, legend_loc="upper left", ax=ax1)
fig1.savefig("output/fig_4_Venn_Eggnog_interproscan_fatcat_cath.png", dpi=500)


Eggnog_interproscan_DeepFRI_seq ={"Eggnog":set(Eggnog_all_list),
                                  "InterProScan":set(InterProScan_all_list),
                                  "DeepFRI-sequence":set(DeepFRI_seq_all_list)
                                  }

# Venn - Eggnog-interproscan-DeepFRI-sequence
fig1, ax1 = plt.subplots(figsize=(11.69,8.27), layout='constrained')  
ax1 = venn(Eggnog_interproscan_DeepFRI_seq, cmap=cmaps, fontsize=10, legend_loc="upper left", ax=ax1)
fig1.savefig("output/fig_5_Venn_Eggnog_interproscan_DeepFRI_seq.png", dpi=500)

FATCAT_CATH_DeepFRI_structure = {"FATCAT-CATH":set(FATCAT_CATH_all_list),
                                 "DeepFRI-structure":set(DeepFRI_structure_all_list)
                                       }

# Venn - FATCAT_CATH_DeepFRI_structure
fig1, ax1 = plt.subplots(figsize=(11.69,8.27), layout='constrained')  
ax1 = venn(FATCAT_CATH_DeepFRI_structure, cmap=cmaps, fontsize=10, legend_loc="upper left", ax=ax1)
fig1.savefig("output/fig_6_Venn_FATCAT_CATH_DeepFRI_structure.png", dpi=500)


Homology_machina_laerning = {"Homology":set(Eggnog_all_list+InterProScan_all_list+FATCAT_CATH_all_list),
                             "Machine_learning":set(DeepFRI_seq_all_list+DeepFRI_structure_all_list)
                                       }
# Venn - Homology_machina_laerning
fig1, ax1 = plt.subplots(figsize=(11.69,8.27), layout='constrained')  
ax1 = venn(Homology_machina_laerning, cmap=cmaps, fontsize=10, legend_loc="upper left", ax=ax1)
fig1.savefig("output/fig_7_Venn_Homology_machina_laerning.png", dpi=500)



data_GO = pd.read_csv("input/4.1_split_into_3_3353_without_SP_R.tsv",sep="\t", index_col=0)

# seq_BP
seq_BP = []
data_seq_BP = data_GO [~(data_GO ["Deepfri_seq_GO_BP"] == "-")]
add_name_in_list(data_seq_BP,seq_BP)

# seq_CC
seq_CC = []
data_seq_CC = data_GO [~(data_GO ["Deepfri_seq_GO_CC"] == "-")]
add_name_in_list(data_seq_CC,seq_CC)

# seq_MF
seq_MF = []
data_seq_MF = data_GO [~(data_GO ["Deepfri_seq_GO_MF"] == "-")]
add_name_in_list(data_seq_MF,seq_MF)

# structure_BP
structure_BP = []
data_structure_BP = data_GO [~(data_GO ["Deepfri_structure_GO_BP"] == "-")]
add_name_in_list(data_structure_BP,structure_BP)

# structure_CC
structure_CC = []
data_structure_CC = data_GO [~(data_GO ["Deepfri_structure_GO_CC"] == "-")]
add_name_in_list(data_structure_CC,structure_CC)

# structure_MF
structure_MF = []
data_structure_MF = data_GO [~(data_GO ["Deepfri_structure_GO_MF"] == "-")]
add_name_in_list(data_structure_MF,structure_MF)

# seq_EC
seq_EC = []
data_seq_EC = data_protein_all_raw[~(data_protein_all_raw["DeeoFri_seq_EC_value"] == "-")]
add_name_in_list(data_seq_EC,seq_EC)

# structure_EC
structure_EC = []
data_structure_EC = data_protein_all_raw[~(data_protein_all_raw["DeeoFri_structure_EC_value"] == "-")]
add_name_in_list(data_structure_EC,structure_EC)

BP = {"seq_BP":set(seq_BP),
      "structure_BP":set(structure_BP)
      }

fig1, ax1 = plt.subplots(figsize=(11.69,8.27), layout='constrained')  
ax1 = venn(BP, cmap=cmaps, fontsize=10, legend_loc="upper left", ax=ax1)
fig1.savefig("output/fig_8_Venn_BP.png", dpi=500)

CC = {"seq_CC ":set(seq_CC),
      "structure_CC ":set(structure_CC)
      }

fig1, ax1 = plt.subplots(figsize=(11.69,8.27), layout='constrained')  
ax1 = venn(CC, cmap=cmaps, fontsize=10, legend_loc="upper left", ax=ax1)
fig1.savefig("output/fig_9_Venn_CC.png", dpi=500)

MF = {"seq_MF ":set(seq_MF),
      "structure_MF ":set(structure_MF)
      }

fig1, ax1 = plt.subplots(figsize=(11.69,8.27), layout='constrained')  
ax1 = venn(MF, cmap=cmaps, fontsize=10, legend_loc="upper left", ax=ax1)
fig1.savefig("output/fig_10_Venn_MF.png", dpi=500)

EC = {"seq_EC ":set(seq_EC),
      "structure_EC ":set(structure_EC)
      }

fig1, ax1 = plt.subplots(figsize=(11.69,8.27), layout='constrained')  
ax1 = venn(EC, cmap=cmaps, fontsize=10, legend_loc="upper left", ax=ax1)
fig1.savefig("output/fig_11_Venn_EC.png", dpi=500)




