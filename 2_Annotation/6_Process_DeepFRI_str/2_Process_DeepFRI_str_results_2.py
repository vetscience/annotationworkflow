import pandas as pd
import numpy as np
##1
f1 = open("output/2_1_Deep_structure_BP_result.txt","r")

structure_BP = {}
lines = f1.readlines()
for line in lines:
    line = line.strip()
    coms = line.split("\t")
    names = coms[0].split("_")
    name = names[1] + "_" + names[2] + "_" + names[3]
    GO = coms[1][:-1]
    structure_BP[name] = GO

print(structure_BP)
import json
json_str = json.dumps(structure_BP, indent=4)
with open("output/structure_BP_GO_dict",'w') as json_file:
    json_file.write(json_str)
##2
f2 = open("output/2_2_Deep_structure_CC_result.txt","r")

structure_CC = {}
lines = f2.readlines()
for line in lines:
    line = line.strip()
    coms = line.split("\t")
    names = coms[0].split("_")
    name = names[1] + "_" + names[2] + "_" + names[3]
    GO = coms[1][:-1]
    structure_CC[name] = GO

print(structure_CC)
import json
json_str = json.dumps(structure_CC, indent=4)
with open("output/structure_CC_GO_dict",'w') as json_file:
    json_file.write(json_str)
##3
f3 = open("output/2_3_Deep_structure_EC_result.txt","r")

structure_EC = {}
lines = f3.readlines()
for line in lines:
    line = line.strip()
    coms = line.split("\t")
    names = coms[0].split("_")
    name = names[1] + "_" + names[2] + "_" + names[3]
    GO = coms[1][:-1]
    structure_EC[name] = GO

print(structure_EC)
import json
json_str = json.dumps(structure_EC, indent=4)
with open("output/structure_EC_num_dict",'w') as json_file:
    json_file.write(json_str)

##4
f4 = open("output/2_4_Deep_structure_MF_result.txt","r")

structure_MF = {}
lines = f4.readlines()
for line in lines:
    line = line.strip()
    coms = line.split("\t")
    names = coms[0].split("_")
    name = names[1] + "_" + names[2] + "_" + names[3]
    GO = coms[1][:-1]
    structure_MF[name] = GO

print(structure_MF)
import json
json_str = json.dumps(structure_MF, indent=4)
with open("output/structure_MF_GO_dict",'w') as json_file:
    json_file.write(json_str)




DeepFri_structure_3395 = {}

f = open("input/Protein_list")
for line in f.readlines():
    line = line.strip()
    GO_list = []
    if line in structure_BP.keys():
        if structure_BP[line] != '-':
            terms = structure_BP[line].split(',')

            for g in terms:
                if g in GO_list:
                    print(g + " duplicated！Please check it BP!")
                GO_list.append(g)

    if line in structure_CC.keys():
        if structure_CC[line] != '-':
            terms = structure_CC[line].split(',')
            for g in terms:
                if g in GO_list:
                    print(g + " duplicated！Please check it CC!")
                GO_list.append(g)
    if line in structure_MF.keys():
        if structure_MF[line] != '-':
            terms = structure_MF[line].split(',')
            for g in terms:
                if g in GO_list:
                    print(g + " duplicated！Please check it MF!")
                GO_list.append(g)

    if len(GO_list) == 0:
        DeepFri_structure_3395[line] = '-'
    if len(GO_list) == 1:
        DeepFri_structure_3395[line] = GO_list[0]
    if len(GO_list) > 1:
        contents = GO_list[0]
        for unit in GO_list:
            contents = contents + ',' + unit
        DeepFri_structure_3395[line] = contents






print(len(DeepFri_structure_3395))
import json
json_str = json.dumps(DeepFri_structure_3395, indent=4)
with open("output/DeepFri_structure_3395_without_SP.json",'w') as json_file:
    json_file.write(json_str)

# for score
def load_dict(path):
    f = open(path,"r")
    return json.load(f)

score_dict_BP  = load_dict("./output/Scores/structure_BP_score_dict.json")
score_dict_CC  = load_dict("./output/Scores/structure_CC_score_dict.json")
score_dict_MF  = load_dict("./output/Scores/structure_MF_score_dict.json")
Score_list = []
def get_the_average_score(name_j,BP_dict,CC_dict,MF_dict):
    list_3 = []
    if name_j in BP_dict.keys():
        BP_S = BP_dict[name_j]
        list_3.append(float(BP_S))

    if name_j in CC_dict.keys():
        CC_S = CC_dict[name_j]
        list_3.append(float(CC_S))

    if name_j in MF_dict.keys():
        MF_S = MF_dict[name_j]
        list_3.append(float(MF_S))

    if len(list_3) == 0:
        score_3 = '-'
    else:
        score_3 = np.mean(list_3)
    return score_3


f_protein_list = open("input/Protein_list")
Protein_name_list = []
GO_results_list = []

EC_dict  = load_dict("./output/structure_EC_num_dict") 
EC_list = [] 

for j in f_protein_list.readlines():
    j = j.strip()
    if j in DeepFri_structure_3395.keys():
        GO_results = DeepFri_structure_3395[j]
    else:
        GO_results = '-'

    if j in EC_dict.keys():     
        EC_value = EC_dict[j]   
    else:                       
        EC_value = '-'          
    EC_list.append(EC_value)    

    score_value = get_the_average_score(j,score_dict_BP,score_dict_CC,score_dict_MF) 
    Score_list.append(score_value) 

    Protein_name_list.append(j)
    GO_results_list.append(GO_results)

data6 = pd.DataFrame(
    {
        "Deepfri_structure_GO":GO_results_list,
        "DeeoFri_structure_G0_score": Score_list, 
        "DeeoFri_structure_EC_value": EC_list 
    }
)

data6.index = Protein_name_list

data6.to_csv('Path_to_output',sep='\t')