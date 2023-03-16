import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_and_process_data(file_path):
    data = pd.read_csv(file_path, sep="\t", index_col=0)
    return data

def filter_data(data):
    subsets = {}

    base_conditions = [
        ~(data["Eggnog_Description"] == "-"),
        ~(data["Eggnog_EC"] == "-"),
        ~(data["Eggnog_KEGG_ko"] == "-"),
        ~(data["Eggnog_KEGG_Pathway"] == "-"),
        ~(data["Eggnog_Pfam"] == "-"),
        ~(data["Eggnog_KEGG_Module"] == "-"),
        ~(data["Eggnog_KEGG_Reaction"] == "-"),
        ~(data["Eggnog_KEGG_rclass"] == "-"),
        ~(data["Eggnog_KEGG_TC"] == "-"),
        ~(data["Eggnog_BRITE"] == "-"),
        ~(data["Eggnog_CAZy"] == "-"),
        ~(data["Eggnog_BiGG_Reaction"] == "-"),
        ~(data["InterProScan_InterPro_hit"] == "-"),
        ~(data["InterProScan_Pathway"] == "-"),
        ~(data["Eggnog_GOs"] == "-"),
        ~(data["InterProScan_GO"] == "-"),
    ]

    eggnog_interproscan_conditions = base_conditions.copy()
    subsets['eggnog_interproscan'] = data[np.logical_or.reduce(eggnog_interproscan_conditions)]

    fatcat_cath_conditions = base_conditions + [
        ~(data["CATH_hit_structure"] == "-"),
        ~(data["CATH_GO"] == "-"),
    ]
    subsets['eggnog_interproscan_fatcat_cath'] = data[np.logical_or.reduce(fatcat_cath_conditions)]

    deepfri_conditions = fatcat_cath_conditions + [
        ~(data["DeeoFri_seq_EC_value"] == "-"),
        ~(data["DeeoFri_structure_EC_value"] == "-"),
        ~(data["combined_GO"] == "-"),
    ]
    subsets['eggnog_interproscan_fatcat_cath_deepfri'] = data[np.logical_or.reduce(deepfri_conditions)]

    return subsets

def create_pie_charts(subsets, file_name_prefix):
    subset_lengths = [len(subset) for subset in subsets.values()]
    dark_matter = 3353 - subset_lengths[-1]

    fig, ax = plt.subplots()
    ax.pie(subset_lengths + [dark_matter],
           labels=['Eggnog and InterProScan', 'FATCAT-CATH', 'DeepFRI', 'Dark_matter'],
           colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"],
           explode=(0, 0.2, 0, 0),
           autopct='%.2f%%')

    plt.show()
    fig.savefig(f"{file_name_prefix}_pie_plot.png")

def main():
    file_path = "PATH_TO_INPUT"
    data = read_and_process_data(file_path)
    subsets = filter_data(data)
    create_pie_charts(subsets, "PATH_TO_OUTPUT")

if __name__ == "__main__":
    main()
