import sys
import subprocess

# Check command-line arguments
if len(sys.argv) != 3:
    print("Please provide the input file name and output file name as command-line arguments.")
    print("Example: python3 script.py input_file.fa output_file.out")
    sys.exit(1)

# Get command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Build command
command = f'''
    source activate eggnog && \
    export EGGNOG_DATA_DIR=/home/XXX(your own path)/Annotation/Eggnog/database && \
    emapper.py -i {input_file} -o {output_file} --cpu 40
'''

# Run command in Linux
subprocess.call(command, shell=True)


