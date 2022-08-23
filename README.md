# Intro To biology
## Poorvi H C

## The given folder has programs as follows:
<!-- ``` -->
- `Ndistance.ipynb`
- `UPGMA_RNA.py`
- `Pdistance.py`
- `UPGMA_Protien.py`

<!-- ``` -->

## Required modules for running the program:
```
    pip install numpy
    pip install alignment
    pip install blosum
```
### - When faced with errors regarding missing modules, follow the format `pip install <module name>` and install the required modules.

Running `Ndistance.ipynb` produces the csv file `Ndistance.csv` in the Ouput folder, which stores the distance matrix for the given RNA sequences.
The distance here is such that the smaller it is, the closer the sequences are. 
`UPGMA_RNA.py` reades this csv file and prints the Phylogenetic tree for the sequences.

Similarly, running `Pdistance.py` produces the csv file `Pdistance.csv`, which stores the distance matrix for the Protein sequences.
The distance here is such that the larger it is, the closer the sequences are.
`UPGMA_Protien.py` reads this csv file and prints the Phylogenetic tree for the sequences.

#### The Folder contains all the things one needs to run the program and get the phylogenetic tree printed on the terminal. There are 3 folders included, namely:
- `Input`
- `Output`
- `Phylogenetic Tree`

The `Input` folder contains the sample input files in the form of `Nucleotide.txt` and `Protien.txt`, which give more information on the format of the input expected.

The `Output` folder contains the Output .csv files, while the `Phylogenetic Tree` folder contains the images of the ideal trees that need to be generated for the sample inputs.

#### How to use this project?

 1. Make sure the input files are in the `Input` folder, and are of the same format as the sample `Nucleotide.txt` and `Proteins.txt`.
 2. Run all the cells in `Ndistance.ipynb`. 
 3. After it is done running, run `python UPGMA_RNA.py`, if using a conda environment or runrun `python3 UPGMA_RNA.py` . The phylogenetic tree will be printed in the terminal.
 4. Similarly, run the respective files in the same format as shown above.

