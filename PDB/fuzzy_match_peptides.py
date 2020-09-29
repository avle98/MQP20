####
# Le Gall Lab at Ragon Institute of MIT, Harvard, and MGH
# Ann Le
# June 2018
# Last Updated: July 25, 2018
# Protocol Name: Fuzzy Matching
# This code reads in two text files and prints out the fuzzy matches (approximate string matching) using the
# Levenshtein distance algorithm for one list of sequences against another list of sequences.
####

from fuzzywuzzy import process


def fuzzy_match(seq_txt, cyto_txt):

    # open both text files
    with open(seq_txt, 'r') as a, open(cyto_txt, 'r') as b:
        sequences = a.readlines() # read first text file
        cytosolseq = b.readlines() # read second text file

    # for each string in the first list from the first text file
    for i in sequences:
        # find the best matches from the second list with a limit of 300 results and a score cutoff of 50
        match = process.extractBests(i, cytosolseq, limit=300, score_cutoff=50)
        matches = str(match) # make the matches strings
        print matches.strip("[]''") # print and strip the strings of the following characters

    a.close() # close the first text file
    b.close() # close the second text file

# change the path and name of the first and second text file to run this program
fuzzy_match('/Users/legalllab/Documents/PDB/Example Files/seqs.txt', '/Users/legalllab/Documents/PDB/Example Files/cytoseq.txt')




