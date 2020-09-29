####
# Le Gall Lab at Ragon Institute of MIT, Harvard, and MGH
# Ann Le
# June 2017
# Last Updated: June 2017
# Protocol: N/A
# This code opens the text file from one PDB accession numbers and then creates
# another text file with information of secondary structure of that peptide
####

import urllib2

# opens the designated website
website = urllib2.urlopen('http://www.uniprot.org/uniprot/P14174.txt')
URL = website.geturl()

# prints out information about the website
header = website.info()
date = header['Date']
last_mod = header['Last-Modified']

# prints out information about peptide in website
data = website.readlines()
lists = []
for word in data:
    if word.startswith('ID '):
        lists.append(word)
    if word.startswith('AC '):
        lists.append(word)
    if word.startswith('FT '):
        lists.append(word)

strings = ''.join(lists)

# write information into a text file onto computer
with open('/Users/legalllab/Documents/PDB/results.txt', 'w') as f:
    f.write('URL ' + URL + '\n')
    f.write('Run Date: ' + date + '\n')
    f.write('Last Modified: ' + last_mod + '\n')
    f.write(strings)
f.close()

print 'Successful!'

