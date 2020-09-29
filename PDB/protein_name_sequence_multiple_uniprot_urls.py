####
# Le Gall Lab at Ragon Institute of MIT, Harvard, and MGH
# Ann Le
# June 2017
# Last Updated: July 2018
# Protocol Name: Protein Information Through Multiple UniProt URLs
# This code opens the text file with the Uniprot URLs and then creates
# another text file with information about the peptide.
####

from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import csv

def get_protein_information (uniprot_urls_txt):

    # open text file of all urls for unipro
    quote_page = open('/Users/legalllab/Documents/PDB/PeptideIDresults.txt')

    # print column titles
    print 'Accession_number ' + 'Protein_ID ' + 'Sequence ' + 'Length ' + 'Mass(Daltons)'

    # for loop to put all information into dictionary
    for pg in quote_page:
        print  # have a break between each protein
    # query website and return the html to the  variable 'site'
        page = urllib2.urlopen(pg).read()
    # parse html using beautiful soup and store in variable 'soup'
        soup = BeautifulSoup(page, 'html.parser')

        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []

    # get the peptide information
        span_id = soup.find('span', {'id': 'entrySequence'}).getText()
        accessions = span_id[4:10]
        # print
        #  accessions
        list1.append(accessions)

    # get the protein information
        id_name = soup.find('title').getText()
        protein = id_name[:id_name.find('-')]
        # print protein
        list2.append(protein)

    # get the sequence information
        seq = soup.find('span', {'id': 'entrySequence'}).getText()
        seqs = seq.split('\n')
        seqss = seqs[1:]
        seqsss = ''.join(seqss)
        # print seqsss
        list3.append(seqsss)

    # get length and mass information
        len_and_mass = soup.find('div', attrs={'class': 'sequence-isoform-rightcol'})
        spans = len_and_mass.findAll('span')
        for length in spans[1]:
            # print length
            list4.append(length)
        for mass in spans[3]:
            # print mass
            list5.append(mass)

        for a, b, c, d, e in zip(list1, list2, list3, list4, list5):
            print a, b, c, d, e

    print
    print "Successful!"  # will print if everything is successful


# change 'uniprot_urls_txt' to the name of your created file of all UniProt URLs
get_protein_information ('/Users/legalllab/Documents/PDB/UniprotURLS/.txt')