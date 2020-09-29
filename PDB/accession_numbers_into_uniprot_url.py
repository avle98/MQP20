####
# Le Gall Lab at Ragon Institute of MIT, Harvard, and MGH
# Ann Le
# June 2017
# Last Updated: June 2017
# Protocol Name: Protein Information Through Multiple UniProt URLs
# This code opens the text file with the PDB accession numbers and then creates
# another text file with uniprot urls for all of the accession numbers
####


# open text file with all the accession numbers
# change 'accessions' to name and path of created file with accession numbers
with open('/Users/legalllab/Documents/PDB/Example Files/quentin.txt', 'r') as f:
    accession = f.readlines()  # read lines of accession file

# add the accession number to the end of the url
    website = ['http://www.uniprot.org/uniprot/' + line for line in accession]
    print(website)

# open text file called urls
# change name and path of 'urls' to whatever you want to name your file with the uniprot urls
with open('/Users/Desktop/HLAA.txt', 'w') as p:
    p.writelines(website) # write websites into the new file

f.close() # close accessions.txt
p.close() # close urls.txt
