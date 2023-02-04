import numpy as np

def parse_file(input_path,output_path,score_path):
    f = open(input_path, "r")
    lines = f.readlines()[2:]
    Name_GO = {}
    Name_Score = {}  

    for line in lines:
        line = line.strip()
        com = line.split(",")

        Name = com[0]
        GO = com[1]
        Score = com[2]
        description = com[3]



        if float(Score) > 0.5:  
            Name_GO[Name] = []
            Name_Score[Name] = []  

    for line in lines:
        line = line.strip()
        com = line.split(",")

        Name = com[0]
        GO = com[1]
        Score = com[2]
        description = com[3]

        if float(Score) > 0.5:
            Name_GO[Name].append(GO)
            Name_Score[Name].append(float(Score))  

    print(Name_GO)

    print(len(Name_GO.keys()))

    name_list = sorted(Name_GO.keys(), key=lambda x: int(x.split("_")[0])) 

    f_result = open(output_path,"w")

    for item in name_list:
        if Name_GO[item] == "-":
            f_result.write(item+"\t"+str(Name_GO[item])+"\n")
        else:
            go_term = ""
            for go in Name_GO[item]:
                go_term = go + "," + go_term
            f_result.write(item+"\t"+go_term+"\n")


    f_result.close()


    Final_score_dict = {}

    print(Name_Score)

    for i in Name_Score.keys():
        i_1 = i.split("_")
        i_2 = i_1[1] + "_" + i_1[2] + "_" + i_1[3]
        Final_score_dict[i_2] = np.mean(Name_Score[i])  
    import json
    json_str = json.dumps(Final_score_dict, indent=4)
    with open(score_path,'w') as json_file:
        json_file.write(json_str)



input_path = "input/DeepFRI_BP_predictions.csv"
output_path = "output/2_1_Deep_structure_BP_result.txt"
score_path = "output/Scores/structure_BP_score_dict.json"
parse_file(input_path, output_path, score_path)

input_path = "input/DeepFRI_CC_predictions.csv"
output_path = "output/2_2_Deep_structure_CC_result.txt"
score_path = "output/Scores/structure_CC_score_dict.json"
parse_file(input_path, output_path, score_path)

input_path = "input/DeepFRI_EC_predictions.csv"
output_path = "output/2_3_Deep_structure_EC_result.txt"
score_path = "output/Scores/structure_EC_score_dict.json"
parse_file(input_path, output_path, score_path)

input_path = "input/DeepFRI_MF_predictions.csv"
output_path = "output/2_4_Deep_structure_MF_result.txt"
score_path = "output/Scores/structure_MF_score_dict.json"
parse_file(input_path, output_path, score_path)