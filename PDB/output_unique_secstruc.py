####
# Le Gall Lab at Ragon Institute of MIT, Harvard, and MGH
# Ann Le
# May 2018
# Last Updated: May 17, 2018
# Protocol Name: N/A
# This code allows you to copy and paste the repeated secondary structure columns of helices, strands, and turns
# into a text file. The script will put the unique elements in a list and count the number of
# unique elements, which will all be printed in a new text file for the corresponding secondary structure.
####

def unique_file(input_filename, output_filename):
    input_filename = open (input_filename, 'r')
    file_contents = input_filename.read()

    word_list = file_contents .split() # all of the numbers will be split into separate elements
    duplicates = [] # list called duplicates

    # open a file to write the unique information
    file = open(output_filename, 'w')

    numofwords = 0 # initialize the number of unique words
    for unique_words in word_list:
        if unique_words not in duplicates: # if the split single element is not in the duplicates list,
            duplicates.append(unique_words) # add it into the duplicates list
            numofwords += 1 # count by 1 each time a unique word is added into the duplicates list
            file.write(str(unique_words) + "\n") # write the unique words in the duplicate list with a line break after each
    file.write(str("Number of unique elements: ") + str(numofwords)) # write the amount of unique words

    # close the files
    input_filename.close()
    file.close()


# run the above function for the copied information from the text files for helices, strands, and turns
unique_file('/Users/legalllab/Documents/PDB/SecStructure/ss_helices.txt','/Users/legalllab/Documents/PDB/SecStructure/ss_uniquehelices.txt')
unique_file('/Users/legalllab/Documents/PDB/SecStructure/ss_strands.txt','/Users/legalllab/Documents/PDB/SecStructure/ss_uniquestrands.txt')
unique_file('/Users/legalllab/Documents/PDB/SecStructure/ss_turns.txt','/Users/legalllab/Documents/PDB/SecStructure/ss_uniqueturns.txt')



