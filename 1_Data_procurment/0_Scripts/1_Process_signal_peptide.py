f = open("Path_to_input_file","r")
f1 = open("Path_to_input_file.csv", "w")
lines = f.readlines()
for line in lines:
    line = line.strip()
    coms = line.split(",")
    name = coms[0]+"_without_SP"
    pep_original = coms[1]
    cut_position = int(coms[2])
    pep_new = pep_original[cut_position:]
    print(name)
    print(cut_position)
    print(pep_original)
    print(pep_new)
    f1.write(name+","+pep_new+"\n")



f.close()
f1.close()