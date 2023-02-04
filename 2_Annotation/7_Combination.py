import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_eggnog = pd.read_csv("Path_to_input",sep="\t", index_col=0)
data_InterProScan = pd.read_csv("Path_to_input",sep="\t", index_col=0)
data_CATH = pd.read_csv("Path_to_input",sep="\t", index_col=0)
data_DeepFri_seq = pd.read_csv("Path_to_input",sep="\t", index_col=0)
data_DeepFri_structure = pd.read_csv("Path_to_input",sep="\t", index_col=0)

data_5 = pd.concat([data_eggnog,data_InterProScan,data_CATH,data_DeepFri_seq,data_DeepFri_structure], axis=1)

data_5.to_csv('Path_to_output',sep='\t')

data_GO = data_5[["Eggnog_GOs", "InterProScan_GO","CATH_GO","Deepfri_seq_GO","Deepfri_structure_GO",\
                  "CATH_Pvalue","DeeoFri_seq_G0_score","DeeoFri_structure_G0_score"]]
data_GO.to_csv('Path_to_output',sep='\t')