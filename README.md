# Protein Annotation Workflow

This GitHub repository contains a protein annotation workflow that can be used to annotate protein sequences for various species. The workflow is divided into three stages: data procurement, annotation, and visualization.

## Data Procurement

The data procurement stage includes three operations:

1. Operation of signal peptide: This operation identifies/removes signal peptides in protein sequences using tools like Phobius (Käll et al., 2004, 2007).
2. Operation of structure modelling: This operation predicts protein structures using tools like AlphaFold (Jumper et al., 2021).
3. Operation of quality control: This operation ensures that the protein sequences are of high quality by removing redundant sequences and checking for errors.

## Annotation

The annotation stage includes six operations:

1. EggNOG (Cantalapiedra et al., 2021): This operation assigns functional annotations to protein sequences using EggNOG.
2. InterProScan (Jones et al., 2014) : This operation searches protein sequences against multiple databases and predicts functional domains and sites.
3. DeepFRI-seq (Gligorijević et al., 2021): This operation predicts protein function using deep learning models trained on protein sequence.
4. DeepFRI-str (Gligorijević et al., 2021): This operation predicts protein function using deep learning models trained on protein structure data.
5. FATCAT-CATH (Sillitoe et al., 2019; Li et al., 2020): This operation compares protein structures to a database of known structures and assigns functional annotations.
6. Operation of combination: This operation combines the results from the previous operations to generate a final set of annotations.


## Visualization
   
The visualization stage includes two operations:

1. GO visualization: This operation visualizes the Gene Ontology (GO) terms associated with the annotated proteins.
2. Upset-plot (Lex et al., 2014): This operation visualizes the overlap between the annotated proteins and different datasets.
 
   
## Usage

To use this workflow, follow these steps:
1. Clone the repository to your local machine.
2. Install the required software and dependencies (list them here).
3. Prepare your input data in the appropriate format (list the requirements here).
4. Modify the workflow stages as needed for your species of interest.
5. Run the workflow using the provided scripts and configuration files.

## Installation

Before running the workflow, you will need to install the required software and dependencies. The following software and libraries are required:

Python (version 3.5 or higher)
Phobius (https://phobius.sbc.su.se/data.html)
Alphafold (https://github.com/deepmind/alphafold)
EggNOG (version 2.0 or higher)
InterProScan (version 5.5 or higher)
DeepFRI (https://github.com/flatironinstitute/DeepFRI)
FATCAT (https://fatcat.godziklab.org/)
UpSetPlot (version 0.8 or higher)

You can install these dependencies using the package manager of your choice (e.g., pip, conda, etc.). Make sure to install the correct version of each software.

## Input Data
To run the workflow, you will need input data in the appropriate format. The input data should be a FASTA file containing the protein sequences you wish to annotate. Make sure that the FASTA file follows the standard format, with one sequence per entry and a header line starting with ">".

## Configuration
The workflow can be configured using the provided configuration files. The configuration files specify the parameters for each operation and can be modified as needed for your species of interest. Make sure to specify the correct paths for the input files and software dependencies in the configuration files.

## Running the Workflow
To run the workflow, simply execute the provided scripts in the correct order. The scripts will run each operation in the appropriate order and generate the output files. Make sure to check the output files for errors and warnings.

## Output
The output of the workflow will be a set of annotated protein sequences in various formats (e.g., text, CSV, etc.). The output files will contain the functional annotations assigned to each protein sequence, 

## Contact

If you have any questions or need more detailed information about this workflow, please don't hesitate to contact us. We are happy to help!
