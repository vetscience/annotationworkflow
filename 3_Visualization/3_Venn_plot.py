import matplotlib.pyplot as plt
import pandas as pd
from venn import venn
import numpy as np

plt.style.use('ggplot')
cmaps = ['#F6B93B', '#E55039', '#4A69BD', '#60A3BC', '#BBEA99']

data_protein_all_raw = pd.read_csv("PATH_to_INPUT", sep="\t", index_col=0)


def get_filtered_data(data, filters):
    return data[~np.logical_and.reduce([data[f] == "-" for f in filters])]


def create_venn_diagram(data, filename, figsize=(11.69, 8.27), layout='constrained'):
    fig, ax = plt.subplots(figsize=figsize, layout=layout)
    ax = venn(data, cmap=cmaps, fontsize=10, legend_loc="upper left", ax=ax)
    fig.savefig(filename, dpi=100)


data_eggnog_all = get_filtered_data(data_protein_all_raw, ["Eggnog_Description", "Eggnog_EC", "Eggnog_KEGG_ko", "Eggnog_KEGG_Pathway", "Eggnog_Pfam", "Eggnog_KEGG_Module", "Eggnog_KEGG_Reaction", "Eggnog_KEGG_rclass", "Eggnog_KEGG_TC", "Eggnog_BRITE", "Eggnog_CAZy", "Eggnog_BiGG_Reaction", "Eggnog_GOs"])
data_interproscan_all = get_filtered_data(data_protein_all_raw, ["InterProScan_InterPro_hit", "InterProScan_Pathway", "InterProScan_GO"])
data_fatcat_cath_all = get_filtered_data(data_protein_all_raw, ["CATH_hit_structure", "CATH_GO"])
data_deepfri_seq_all = get_filtered_data(data_protein_all_raw, ["DeeoFri_seq_EC_value", "Deepfri_seq_GO"])
data_deepfri_structure_all = get_filtered_data(data_protein_all_raw, ["DeeoFri_structure_EC_value", "Deepfri_structure_GO"])

venn_data = {
    "Eggnog_InterProScan_FATCAT_CATH": {"Eggnog": set(data_eggnog_all.index), "InterProScan": set(data_interproscan_all.index), "FATCAT-CATH": set(data_fatcat_cath_all.index)},
    "Eggnog_InterProScan_DeepFRI_seq": {"Eggnog": set(data_eggnog_all.index), "InterProScan": set(data_interproscan_all.index), "DeepFRI-sequence": set(data_deepfri_seq_all.index)},
    "FATCAT_CATH_DeepFRI_structure": {"FATCAT-CATH": set(data_fatcat_cath_all.index), "DeepFRI-structure": set(data_deepfri_structure_all.index)},
    "Homology_Machine_learning": {"Homology": set(data_eggnog_all.index).union(data_interproscan_all.index).union(data_fatcat_cath_all.index), "Machine_learning": set(data_deepfri_seq_all.index).union(data_deepfri_structure_all.index)}
}

for name, data in venn_data.items():
    create_venn_diagram(data, f"3.1_Example_output_{name}.png")
