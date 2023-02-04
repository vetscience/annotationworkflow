#!/bin/bash
#SBATCH -A punim0457
#SBATCH --job-name=alphafold
#SBATCH --nodes=1
#SBATCH --partition gpgpu
#SBATCH --gres=gpu:p100:1
#SBATCH --cpus-per-task=4
#SBATCH --time=5-0:0:0
#SBATCH --cpus-per-task=8
#SBATCH --output outAlpha
#SBATCH --error errAlpha
#SBATCH --mem=150G

#The project directory will be made available inside the Alphafold Singularity Container environment
PROJDIR="Path_to_input"
DATASET="/data/scratch/datasets/alphafold/"

module load singularity/3.7.3

ls *fa | while read line; do

singularity exec --nv     \
    --env TF_FORCE_UNIFIED_MEMORY=1,XLA_PYTHON_CLIENT_MEM_FRACTION=4.0 \
    -B $DATASET/:$DATASET/  \
    -B $PROJDIR:$PROJDIR \
    /data/scratch/projects/punim0457/WillData/AF_shared/alphafold-2.1.0.sif    \
        /app/run_alphafold.sh       --data_dir=$DATASET   \
           --uniref90_database_path=$DATASET/uniref90/uniref90.fasta  \
           --mgnify_database_path=$DATASET/mgnify/mgy_clusters_2018_12.fa  \
           --pdb70_database_path=$DATASET/pdb70/pdb70  \
           --template_mmcif_dir=$DATASET/pdb_mmcif/mmcif_files/  \
           --obsolete_pdbs_path=$DATASET/pdb_mmcif/obsolete.dat  \
           --bfd_database_path=$DATASET/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt  \
           --uniclust30_database_path=$DATASET/uniclust30/uniclust30_2018_08/uniclust30_2018_08       \
           --fasta_paths=$PROJDIR/"$line"  \
           --max_template_date=2020-05-14       \
           --model_preset=monomer       \
           --output_dir=$PROJDIR/output_"$line"         \
           -v 1
done