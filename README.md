# Protein Annotation Workflow

This GitHub repository contains a protein annotation workflow that can be used to annotate protein sequences for various species. The workflow is divided into three stages: data procurement, annotation, and visualization.

## Data Procurement

The data procurement stage includes three operations:

1. Operation of signal peptide: This operation identifies signal peptides in protein sequences using tools like Phobius (Käll et al., 2004, 2007).
2. Operation of structure modelling: This operation predicts protein structures using tools like Alphafold (Jumper et al., 2021).
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

## Contact

If you have any questions or need more detailed information about this workflow, please don't hesitate to contact us. We are happy to help!
