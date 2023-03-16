import matplotlib.pyplot as plt

input_file = "path_to_input_file"
output_file_1 = "path_to_output_file_1"
output_file_2 = "path_to_output_file_2"

try:
    with open(input_file) as f:
        dic_AA = {}
        for line in f:
            if "ATOM" in line:
                position = line[22:26].strip()
                plddt = line[61:66].strip()
                residue = line[17:20].strip()
                dic_AA[position] = plddt

    if not dic_AA:
        raise ValueError("No 'ATOM' lines found in input file.")

    X, Y = zip(*[(int(k), float(v)) for k, v in dic_AA.items()])

    if not X or not Y:
        raise ValueError("Unable to extract 'position' and/or 'plddt' values from input file.")

    plt.plot(X, Y)
    plt.xlabel('Residue')
    plt.ylabel('Plddt value')
    plt.savefig(output_file_1)
    plt.show()

    with open(output_file_2, 'w') as f:
        for key, value in dic_AA.items():
            f.write(f"{key}\t{value}\n")

except FileNotFoundError:
    print(f"Error: input file '{input_file}' not found.")
except ValueError as e:
    print(f"Error: {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")
