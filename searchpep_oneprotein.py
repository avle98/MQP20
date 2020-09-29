import pymol
import re


def peptide(file):
    f = open(file, 'r')
    for lines in f.readlines():
        word = re.findall(r"[\w']+", lines)
    pdb = word[0]
    peptides = word[1:]

    cmd.fetch(pdb)
    cmd.show_as("cartoon", pdb)
    cmd.color('white', selection="(all)")

    cmd.set('seq_view', 1)
    cmd.set('seq_view_format', 0)
    cmd.set('seq_view_label_spacing', 5)


    cmd.color('tv_red', selection="ss h") #select helices
    cmd.color('marine', selection="ss s") #select sheets
    cmd.color('lime', selection="ss l+") #select loops


    for i in range(len(peptides)):
        cmd.select('pep', ("pepseq "+ peptides[i]))
        cmd.color('gold', 'pep')
        pep_type = cmd.dss('pep', -4)
        print (peptides[i]), (pep_type)


    print ('Succesful!')

cmd.reinitialize()
peptide('/Users/legalllab/PycharmProjects/Pymol/PDB.txt')

