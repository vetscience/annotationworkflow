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
    cd /home/XXX(your own path)/Annotation/FATCAT && \
    cp -r {input_file} ./structures_folder && \
    ls dompdb/* > pdb.list && \
    sed s'/\.pdb//1' pdb.list > tmp; mv tmp pdb.list && \
    split -l 40000 pdb.list pdb.split && \
    ls ./structures_folder/*pdb |  while read line; do
    QUERY=$line
    for i in pdb.split*; do
    FATCATSearch $QUERY $i -time -f $QUERY.$i.output.log -o $QUERY.$i.out.txt
    done
    cat $QUERY.pdb.split*.out.txt > $QUERY.alignment.txt
    rm $QUERY.pdb.split*.out.txt
    fatcatparser.pl -a $QUERY.alignment.txt -f report -o $QUERY.alignment.summary.txt
    done
    exit
'''

# Run command in Linux
subprocess.call(command, shell=True)

command1 = f'''
    cp /home/XXX(your own path)/Annotation/FATCAT/structures_folder/*.alignment.txt {input_file_2} && \
    cp /home/XXX(your own path)/Annotation/FATCAT/structures_folder/*.alignment.summary.txt {input_file_2} && \
    rm -r /home/XXX(your own path)/Annotation/FATCAT/structures_folder
'''

# Run command in Linux
subprocess.call(command1, shell=True)







