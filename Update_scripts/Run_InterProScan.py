import sys
import subprocess

# Check command-line arguments
if len(sys.argv) != 2:
    print("Please provide the input file name as a command-line argument.")
    print("Example: python3 script.py input_file.fa")
    sys.exit(1)

# Get command-line arguments
input_file = sys.argv[1]

# Build command
command = f'''
    source activate interproscan && \
    /home/XXX(your own path)/Annotation/Introproscan/interproscan-5.56-89.0/interproscan.sh -i {input_file} -f tsv -dp -goterms -pa
'''

# Run command in Linux
subprocess.call(command, shell=True)

