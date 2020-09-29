####
# Le Gall Lab at Ragon Institute of MIT, Harvard, and MGH
# Ann Le
# July 2017
# Last Updated: July 18, 2018
# Protocol Name: Analyzing Secondary Structure Through Multiple UniProt URLs
# This code takes in a text file of Uniprot URLS and prints all the secondary structure information along with the
# corresponding peptide strings for each secondary structure.
####

from bs4 import BeautifulSoup
import urllib2

def find_ss_uniprot(url_text_file):

    # open text file of all urls for uniprot
    quote_page = open(url_text_file)

    # print column titles
    print 'Accession_Number_Secondary_Structure_Availability ' + \
          'SEQ ' + 'H_START ' + 'H_END ' 'H_LEN ' + 'S_START ' + 'S_END ' +'S_LEN ' + 'T_START ' + 'T_END ' + 'T_LEN ' + \
            ' ' + ' HELICES ' 'H_PEP ' + 'STRANDS ' + 'S_PEP ' + 'TURNS ' + 'T_PEP '

    # a for loop to find information from all uniprot urls
    for pg in quote_page:
        print  # have a break between each protein
        page = urllib2.urlopen(pg).read() # query website and return the html to the variable 'site'
        soup = BeautifulSoup(page, 'html.parser') # parse html using beautiful soup and store in variable 'soup'

        # scrape out the peptide accession number
        span_id = soup.findAll('span', {'id': 'entrySequence'})

        # scrape out whether a secondary structure is detected
        second_structure = soup.find('div', {'id': 'secondarystructure'})
        if second_structure: # when you find secondary structure
            for accessions in span_id: # for accession number
                print 'Available:' + accessions.getText()[4:10]  # print message and get peptide accession number
        else:  # if you can't find secondary structure
            for accessions in span_id: # for accession number
                print 'Not_available:' + accessions.getText()[4:10]  # print message and get peptide accession number


        # create empty lists for uniprot information to be stored in all of them
        listsequences = []
        hs = []
        he = []
        hlen = []
        ss = []
        se = []
        slen= []
        ts = []
        te = []
        tlen = []
        listhelices = []
        liststrands = []
        listturns = []


        # find sequence information
        for sequence in soup.findAll('span', attrs={'id': 'entrySequence'}):
            listseq = sequence.getText().splitlines(True)
            seq2 = listseq[1:]
            seq3 = ''.join(seq2)
            listsequences.append(seq3) # add the peptide sequence into the 'listsequences'

        # find helices information
        for helix in soup.findAll('rect', attrs={'class': 'HELIX'}):
            hel = helix['title']
            helices = hel[6:]
            hellista = helices.split('-')[0]
            hellistb = helices.split('-')[1]

            hs.append(hellista)  # add helices start info into 'hs'
            he.append(hellistb)  # add helices end info into 'he'
            hlen.append((int(hellistb))-(int(hellista))+1) # add helices length info into 'hlen'
            listhelices.append(helices) # add the helices range info into 'listhelices'

        # find strands/beta-sheets information
        for strand in soup.findAll('rect', attrs={'class': 'STRAND'}):
            beta = strand['title']
            beta_sheets = beta[7:]
            betalista = beta_sheets.split('-')[0]
            betalistb = beta_sheets.split('-')[1]
            
            ss.append(betalista)  # add betasheet/strand start info into ss
            se.append(betalistb)  # add betasheet/strand end info into se
            slen.append((int(betalistb))-(int(betalista))+1) # add betasheet/strand length info into 'slen'
            liststrands.append(beta_sheets) # add the helices range info into 'liststrands'

        # find turns information
        for turn in soup.findAll('rect', attrs={'class': 'TURN'}):
            turns = turn['title']
            turnss = turns[5:]
            turnslista = turnss.split('-')[0]
            turnslistb = turnss.split('-')[1]

            ts.append(turnslista)  # add turns start info into ts
            te.append(turnslistb)  # add turns end info into te
            tlen.append((int(turnslistb))-(int(turnslista))+1) # add turns length info into 'tlen'
            listturns.append(turnss) # add the turns range info into 'listturns'




        empty = ''  # an empty string to use for spacing later

        # print uniprot information
        for a,b,c,d,e,f,g,h,i,j,k,l in map(None, hs, he, hlen, ss, se, slen, ts, te, tlen, listhelices, liststrands, listturns):
            for accessions in span_id:
                print accessions.getText()[4:10],listsequences,a,b,c,d,e,f,g,h,i,empty,empty,j,empty,k,empty,l



    print "\nSuccessful!"  # will print at the bottom if everything is printed out




# if terminal calls this script then the following will run
if __name__ == '__main__':
    # change 'url_text_file' to the designated path to the name of your created file of all UniProt URLs
    find_ss_uniprot('/Users/legalllab/Documents/PDB/Example Files/Env.txt')

