f = open("path_to_input_file","r")

dic_AA = {}
lines = f.readlines()
for line in lines:
    if "ATOM" in line:
        line = line.strip()
        position = line[22:26]
        plddt = line[61:66]
        residue = line[17:20]
        print(position)
        print(plddt)
        print(residue)
        dic_AA[position]=plddt

print(dic_AA)

f.close()
X = []
Y = []
for key, value in dic_AA.items():
    X.append(int(key))
    Y.append(float(value))

print(X)
print(Y)

import matplotlib.pyplot as plt
plt.plot(X,Y)
plt.xlabel('Residue')
plt.ylabel('Plddt value')
plt.show()