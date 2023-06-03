import sys
import subprocess

# Check command-line arguments
if len(sys.argv) != 3:
    print("Please provide the input file name as a command-line argument.")
    print("Example: python3 script.py absolute_path_input_file_dir absolute_path_dir")
    sys.exit(1)

# Get command-line arguments
input_file = sys.argv[1]
input_file_2 = sys.argv[2]

# Build command
command = f'''
    source activate deepfri && \
    cd /home/XXX(your own path)/Annotation/deepfri/DeepFRI && \
    (time python predict.py --pdb_dir {input_file} -ont {{mf,bp,cc,ec}} -v) >& logs.txt && \
    cp DeepFRI_* {input_file_2} && \
    cp logs.txt {input_file_2}
    '''

# Run command in Linux
subprocess.call(command, shell=True)
