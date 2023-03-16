import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from upsetplot import plot, from_contents

# Set the plotting style, font, and color configurations
plt.style.use('ggplot')

# Read the input data file
data_Protein_all_raw = pd.read_csv("PATH_TO_INPUT", sep="\t", index_col=0)

# Function to add protein names from a dataframe to a list
def add_name_in_list(dataframe, datalist):
    for index, _ in dataframe.iterrows():
        datalist.append(index)

# Process the input data to create separate dataframes and lists for each annotation source
sources = {
    "Eggnog": [("Eggnog_Description", "Eggnog_EC", "Eggnog_KEGG_ko", "Eggnog_KEGG_Pathway", "Eggnog_Pfam", "Eggnog_KEGG_Module", "Eggnog_KEGG_Reaction", "Eggnog_KEGG_rclass", "Eggnog_KEGG_TC", "Eggnog_BRITE", "Eggnog_CAZy", "Eggnog_BiGG_Reaction", "Eggnog_GOs"), "Eggnog_GOs"],
    "InterProScan": [("InterProScan_InterPro_hit", "InterProScan_Pathway", "InterProScan_GO"), "InterProScan_GO"],
    "FATCAT_CATH": [("CATH_hit_structure", "CATH_GO"), "CATH_GO"],
    "DeepFRI_seq": [("DeeoFri_seq_EC_value", "Deepfri_seq_GO"), "Deepfri_seq_GO"],
    "DeepFRI_structure": [("DeeoFri_structure_EC_value", "Deepfri_structure_GO"), "Deepfri_structure_GO"]
}

all_list_dict, go_list_dict = {}, {}
for source, (all_columns, go_column) in sources.items():
    data_all = data_Protein_all_raw[~data_Protein_all_raw[list(all_columns)].eq("-").all(axis=1)]
    data_go = data_Protein_all_raw[~data_Protein_all_raw[go_column].eq("-")]

    all_list, go_list = [], []
    add_name_in_list(data_all, all_list)
    add_name_in_list(data_go, go_list)

    all_list_dict[f"{source} combined annotation"] = all_list
    go_list_dict[f"{source} GO annotation"] = go_list

# Function to create and save UpSet plots
def create_upset_plot(data_dict, filename, facecolor):
    upset_data = from_contents(data_dict)
    fig = plt.figure(figsize=(20, 18))
    plot(upset_data, fig=fig, sort_by="cardinality", subset_size='count', min_degree=1, max_degree=6, show_counts='%d', facecolor=facecolor, element_size=32, sort_categories_by=None)
    plt.savefig(filename, dpi=500)

# Generate UpSet plots
create_upset_plot(all_list_dict, "PATH_TO_OUTPUT.png", '#78E08F')
create_upset_plot(go_list_dict, "PATH_TO_OUTPUT.png", '#60A3BC')

