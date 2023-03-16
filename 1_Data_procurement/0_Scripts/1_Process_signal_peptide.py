import os

# Set file paths
input_file_path = os.path.join("path", "to", "input_file")
output_file_path = os.path.join("path", "to", "output_file.csv")

try:
    # Open input and output files
    with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
        # Iterate over each line in input file
        for line in input_file:
            # Parse line into variables
            name, peptide, cut_position = line.strip().split(",")

            # Modify name and peptide
            name += "_without_SP"
            pep_new = peptide[int(cut_position):]

            # Print and write output
            print(name)
            print(cut_position)
            print(peptide)
            print(pep_new)
            output_file.write(f"{name},{pep_new}\n")

except FileNotFoundError:
    print("Could not open input or output file. Check file paths.")
except Exception as e:
    print("An error occurred:", e)
