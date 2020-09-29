from bs4 import BeautifulSoup
import urllib2
# from tqdm import tqdm
# import time

import re
import csv

# from datetime import datetime


####open text file of all urls for uniprot
# change 'urls' to the name of your created file of all UniProt URLs
quote_page = open('/Users/Ann Le/Documents/R_at_Ragon/urls.txt')

####print column titles
print 'Accession_Number_Secondary_Structure_Availability ' + \
      'HELIX ' + 'HSEQ ' + 'STRAND' + 'TURN'

####for loop to put all information into dictionary
for pg in quote_page:
    print  # have a break between each protein
    ####query website and return the html to the  variable 'site'
    page = urllib2.urlopen(pg).read()
    ####parse html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    ####get the peptide information
    span_id = soup.findAll('span', {'id': 'entrySequence'})
    ####get the secondary structure
    second_structure = soup.find('div', {'id': 'secondarystructure'})
    if second_structure:  # when you find secondarystrucutre
        for accessions in span_id:
            print 'Available:' + accessions.getText()[4:10]  # print message
    else:  # if you can't find secondarystructure
        for accessions in span_id:
            print 'Not_available:' + accessions.getText()[4:10]  # print message

    ####print secondary structure information in 6 separate columns

    list1 = []
    list2 = []
    list3 = []
    list4 = []

    for helix in soup.findAll('rect', attrs={'class': 'HELIX'}):
        helices = helix['title']
        list1.append(helices[6:])  # add helices info into list1

    for strand in soup.findAll('rect', attrs={'class': 'STRAND'}):
        beta_sheets = strand['title']
        list3.append(beta_sheets[7:])  # add betasheet/strand info into list2

    for turn in soup.findAll('rect', attrs={'class': 'TURN'}):
        turns = turn['title']
        list4.append(turns[5:])  # add turns info into list3

    for a, b, c, d in map(None, list1, list2, list3, list4):
        for accessions in span_id:
            print accessions.getText()[4:10]
            print ' ', a, b, c, d

#    for i in tqdm(range(100)):
#        time.sleep(0.01)


#######CODE IDEAS TO BE IMPROVED IF PRINTED DIRECTLY ONTO EXCEL WITHOUT TERMINAL USE
####save data in tuple
##    data.append((span_id, id_name, helices, beta_sheets, turns))


####open a csv file to write information into
##with open('results.csv', 'w') as csvfile:
##    writer = csv.writer(csvfile, delimiter=',')
##    #write colum heads as first line
##    writer.writerow(['Run Date', 'Accession Protein', 'Protein Name', 'Alpha Helices', 'Beta Sheets'])
##
##    #print out the data into columns
##    for span_id, id_name, helices, beta_sheets in data:
##        writer.writerow([datetime.now(), span_id[4:10], id_name[1:id_name.find('-')], helices, beta_sheets]

print "Successful!"  # will print at the bottom if everything is printed out
