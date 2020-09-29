####
# Le Gall Lab at Ragon Institute of MIT, Harvard, and MGH
# Ann Le
# May 2019
# Last Updated: May, 2019
# Protocol Name: Assigning HLA Type
# This code takes in the directory in which it detects a specific type of files, takes the HLA title and assigns
# it to the designated peptide in that file. A text file is then created with all the merged peptides and HLA type.

####


import os
import glob

def assign_HLA(folder, takeaway, merged_file):
    # open directory given in argument
    for filename in glob.iglob(folder):

        with open(filename, 'r') as f:
            # assign path to strip the file name for what was given in the second argument
            path = filename.strip(takeaway)
            # assign root to be the name of the files without the parts designated in takeaway argument
            root, ext = os.path.splitext(path)
            # print the root names in Python console to track progress
            print(root)
            # assign file_lines to be the stripped HLA title and the peptide names together on each line
            file_lines = [''.join([x.strip(), ' ', root, '\n']) for x in f.readlines()]

        with open(merged_file, 'a') as f:
            # write the stripped HLA title name next to the appropriate peptide name on each new line in a new file
            f.writelines(file_lines)
        f.close()



assign_HLA('/Users/legalllab/Desktop/human_immunopeptidome_database_flat/*.txt','/Users/legalllab/Desktop/human_immunopeptidome_database_flat/HLABC','/Users/legalllab/Desktop/HLA_together.txt')


####
# EXPLANATION OF FUNCTION COMMAND ARGUMENTS

# First argument (folder): Provide the directory with all of the HLA text files ('*.txt') of peptide names
# Example is '/Users/legalllab/Desktop/human_immunopeptidome_database_flat/*.txt'

# Second argument (takeaway): What needs to be taken away from the titles of the file names in that directory
# Example is '/Users/legalllab/Desktop/HLAA' or '/Users/legalllab/Desktop/HLAB' or '/Users/legalllab/Desktop/human_immunopeptidome_database_flat/HLAAHLABHLAC'

# Third argument (merged_file_: Provide the name and location of the file you want for the peptides and their HLA names
# Example is '/Users/legalllab/Desktop/HLA_A.txt' or '/Users/legalllab/Desktop/HLA_B.txt' or '/Users/legalllab/Desktop/human_immunopeptidome_database_flat/HLAABC'
####