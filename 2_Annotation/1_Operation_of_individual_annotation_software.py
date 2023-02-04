# EggNOG

emapper.py -i input -o output

# InterProScan

interproscan.sh -i input -f tsv -dp -goterms  -pa 

# FATCAT-CATH

ls dompdb/* > pdb.list
sed s'/\.pdb//1' pdb.list > tmp; mv tmp pdb.list 
split -l 40000 pdb.list pdb.split

ls ./input_folder/*pdb |  while read line; do
QUERY=$line
for i in pdb.split*; do
FATCATSearch $QUERY $i -time -f $QUERY.$i.output.log -o $QUERY.$i.out.txt
done
cat $QUERY.pdb.split*.out.txt > $QUERY.alignment.txt
rm $QUERY.pdb.split*.out.txt
fatcatparser.pl -a $QUERY.alignment.txt -f report -o $QUERY.alignment.summary.txt
done
exit

# DeepFRI-seq

cd /path_to_input_folder/
(time python predict.py --fasta_fn /path_to_input_file/ -ont {mf,bp,cc,ec} -v) >& logs.txt

# DeepFRI-str

cd /path_to_input_folder/
(time python predict.py --pdb_dir /path_to_structure_folder/ -ont {mf,bp,cc,ec} -v) >& logs.txt 
