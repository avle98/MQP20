import pymol
import re


def peptide(file):
    #open file with protein and peptides
    f = open(file, 'r')
    for lines in f.readlines():
        word = re.findall(r"[\w']+", lines)
    pdb = word[0]
    peptides = word[1:]

    #fetch the protein
    cmd.fetch(pdb)
    #show protein in cartoon mode
    cmd.show_as("cartoon", pdb)
    #color entire protein white
    cmd.color('white', selection="(all)")

    #view sequence is turned on
    cmd.set('seq_view', 1)
    cmd.set('seq_view_format', 0)
    cmd.set('seq_view_label_spacing', 5) #sequence is labeled by 5's


    cmd.color('tv_red', selection="ss h") #select helices
    cmd.color('marine', selection="ss s") #select sheets
    cmd.color('lime', selection="ss l+") #select loops

    #for each peptide in TAB annotation
    for i in range(len(peptides)):
        cmd.select('pep', ("pepseq "+ peptides[i])) #select each peptide
        cmd.color('gold', 'pep') #color each peptide gold


    print ('Succesful!')


cmd.reinitialize() #call reinitialize to restart
# change the file name to redirect where the protein-peptide file is
peptide('/Users/legalllab/PycharmProjects/Pymol/PDB.txt')

