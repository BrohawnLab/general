# general

For using traces.py 

  Execute in a conda environment with pandas, matplotlib, seaborn, pyfiglet, and termcolor
  Suggest creating a directory with your csv files and downloading the script to the data directory
  create and activate conda environment and install the packages listed above (I used python 3.8.5)
  execute using python traces.py
  
  functionality to add: 
    subtracting baselines etc...
    GUI using Qt or electron

For distograms and contact map notebook: 
  
  Taken from my (KT) class project for MCB288... 
    the code uses Biopython to parse pdb files to grab residues' CAs and calculate distances between each one of chain A against itself
    and output a multi-dimensional matrix or tensor. This tensor is plotted as a distogram and distances less than 10 angstrom as a contact map.
    Stats from distograms are output after each plot. 
    
    
  Read through code for usage, in brief: 
    -Create text or csv file with a list of pdbs to download and parse and ensure paths are correct.
    
  Will add PCA or tensor analysis, an appropriate metric to score each distogram, and an unsupervised clustering model  
