import pandas as pd
import numpy as np

##1
f1 = open("output/2_1_Deep_seq_BP_result.txt","r")

seq_BP = {}
lines = f1.readlines()
for line in lines:
    line = line.strip()
    coms = line.split("\t")
    names1 = coms[0].split("@")[1]
    names2 = names1.replace("-","_")[:19]
    name = names2
    GO = coms[1][:-1]
    seq_BP[name] = GO

print(seq_BP)
import json
json_str = json.dumps(seq_BP, indent=4)
with open("output/seq_BP_GO_dict",'w') as json_file:
    json_file.write(json_str)
##2
f2 = open("output/2_2_Deep_seq_CC_result.txt","r")

seq_CC = {}
lines = f2.readlines()
for line in lines:
    line = line.strip()
    coms = line.split("\t")
    names1 = coms[0].split("@")[1]
    names2 = names1.replace("-","_")[:19]
    name = names2
    GO = coms[1][:-1]
    seq_CC[name] = GO

print(seq_CC)
import json
json_str = json.dumps(seq_CC, indent=4)
with open("output/seq_CC_GO_dict",'w') as json_file:
    json_file.write(json_str)
##3
f3 = open("output/2_3_Deep_seq_EC_result.txt","r")

seq_EC = {}
lines = f3.readlines()
for line in lines:
    line = line.strip()
    coms = line.split("\t")
    names1 = coms[0].split("@")[1]
    names2 = names1.replace("-","_")[:19]
    name = names2
    GO = coms[1][:-1]
    seq_EC[name] = GO

print(seq_EC)
import json
json_str = json.dumps(seq_EC, indent=4)
with open("output/seq_EC_num_dict",'w') as json_file:
    json_file.write(json_str)

##4
f4 = open("output/2_4_Deep_seq_MF_result.txt","r")

seq_MF = {}
lines = f4.readlines()
for line in lines:
    line = line.strip()
    coms = line.split("\t")
    names1 = coms[0].split("@")[1]
    names2 = names1.replace("-","_")[:19]
    name = names2
    GO = coms[1][:-1]
    seq_MF[name] = GO

print(seq_MF)
import json
json_str = json.dumps(seq_MF, indent=4)
with open("output/seq_MF_GO_dict",'w') as json_file:
    json_file.write(json_str)


###combine_to_one

DeepFri_seq_3395 = {}

f = open("input/Protein_list")
for line in f.readlines():
    line = line.strip()
    GO_list = []
    if line in seq_BP.keys():
        if seq_BP[line] != '-':
            terms = seq_BP[line].split(',')

            for g in terms:
                if g in GO_list:
                    print(g + " duplicated！Please check it BP!")
                GO_list.append(g)

    if line in seq_CC.keys():
        if seq_CC[line] != '-':
            terms = seq_CC[line].split(',')
            for g in terms:
                if g in GO_list:
                    print(g + " duplicated！Please check it CC!")
                GO_list.append(g)
    if line in seq_MF.keys():
        if seq_MF[line] != '-':
            terms = seq_MF[line].split(',')
            for g in terms:
                if g in GO_list:
                    print(g + " duplicated！Please check it MF!")
                GO_list.append(g)

    if len(GO_list) == 0:
        DeepFri_seq_3395[line] = '-'
    if len(GO_list) == 1:
        DeepFri_seq_3395[line] = GO_list[0]
    if len(GO_list) > 1:
        contents = GO_list[0]
        for unit in GO_list:
            contents = contents + ',' + unit
        DeepFri_seq_3395[line] = contents






print(len(DeepFri_seq_3395))
import json
json_str = json.dumps(DeepFri_seq_3395, indent=4)
with open("output/DeepFri_seq_3395_without_SP.json",'w') as json_file:
    json_file.write(json_str)


# make frame_work
# DeepFri_seq_3395
# for score
def load_dict(path):
    f = open(path,"r")
    return json.load(f)

score_dict_BP  = load_dict("./output/Scores/seq_BP_score_dict.json")
score_dict_CC  = load_dict("./output/Scores/seq_CC_score_dict.json")
score_dict_MF  = load_dict("./output/Scores/seq_MF_score_dict.json")
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
# for score


f_protein_list = open("input/Protein_list")
Protein_name_list = []
GO_results_list = []

EC_dict  = load_dict("./output/seq_EC_num_dict") #EC
EC_list = [] #EC



for j in f_protein_list.readlines():
    j = j.strip()
    if j in DeepFri_seq_3395.keys():
        GO_results = DeepFri_seq_3395[j]
    else:
        GO_results = '-'

    if j in EC_dict.keys():     #EC
        EC_value = EC_dict[j]   #EC
    else:                       #EC
        EC_value = '-'          #EC
    EC_list.append(EC_value)    #EC


    score_value = get_the_average_score(j,score_dict_BP,score_dict_CC,score_dict_MF) # for score
    Score_list.append(score_value) # for score

    Protein_name_list.append(j)
    GO_results_list.append(GO_results)

data6 = pd.DataFrame(
    {
        "Deepfri_seq_GO":GO_results_list,
        "DeeoFri_seq_G0_score": Score_list,  # for score
        "DeeoFri_seq_EC_value": EC_list  #EC
    }
)

data6.index = Protein_name_list

data6.to_csv('Path_to_output',sep='\t')




