import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.collocations import *
import math
import os

#get current working directory
cwd = os.getcwd()

##############################################################################
# We want to concatenate every text file in a corpora into one large text
# file so that it is easier to analyze.
##############################################################################


# # First empty out the compiled text file
# f = open('combined_text.txt', 'w')
# f.write('')
# f.close()

# ###############################################################################
# # Now, we want to get all the file names in our corpora, which is in the same
# # directory as our python file. We use these file names to append onto the
# # the large text file, to create one large text file with every text in our
# # corpora
# ###############################################################################

# # pass in CWD, get files using a wild card dilimeter
# # filenames_H = PlaintextCorpusReader(cwd, 'H.*.txt')

# # get our fileids, open up the file, then append it onto our alltext.txt
# for file in filenames_H.fileids():
# 	with open (file, "r") as myfile:
# 		data = myfile.read()
# 		f = open('combined_text.txt', 'a')
# 		f.write(data)

# # making sure the text file is closed
# f.close()

# filenames_N = PlaintextCorpusReader(cwd, 'N.*.txt')

# for file in filenames_N.fileids():
# 	with open (file, "r") as myfile:
# 		data = myfile.read()
# 		f = open('combined_text.txt', 'a')
# 		f.write(data)

# # making sure the text file is closed
# f.close()


#################
# Another option to create the combined files is that we could've used
# the terminal. For Mac we just needed to use the call:
# $cat *.txt > cominbed_files.txt
##################


with open('combined_text.txt', 'r') as myfile:
	text = myfile.read()

bigram_measures = nltk.collocations.BigramAssocMeasures()
tokens = nltk.wordpunct_tokenize(text)
finder = BigramCollocationFinder.from_words(tokens)
finder.apply_word_filter(lambda w: w in
	('\'', ',', '"', '.', ';', '!', '?' ,'s', 't', 'and','the', ',\"',',\'',
		'a','he','had','she','I','you','us','we','them','us', '*', '-', '[',
		']', ':', 'as', 'in', 'to', 'they', '.\"', '!\"', '?\"', '?\"',
		'He', 'because','.','The', '?\"', 'is', 'him', 'her','his',
		',\"', 'It', '\'ll', 'it', ',\"', '.\"' 'my', 'your', 'me', 'was',
		'were', 'would', ',\"', '.\"', '\'', 've', ',\”', '\’', 'll', 'A',
		'{', 'i', 'And', 'THE', 'You', '--', 'í', 'of', 'î'
		))
scored = finder.score_ngrams(bigram_measures.raw_freq)
bigrams = finder.nbest(bigram_measures.raw_freq, 50)

print("Callocations with filters:")
for pair in bigrams:
	print(pair)




finder_raw = BigramCollocationFinder.from_words(tokens)
finder_raw.apply_word_filter(lambda w: w in
	('\'', ',', '"', '.', ';', '!', '?' ,'s', 't', ',\"',',\'',
		'*', '-', '[', ']', ':', '.\"', '!\"', '?\"', '?\"',
		'.', '?\"', ',\"', '\'ll', ',\"', '.\"', 'were', 'would',
		',\"', '.\"', '\'', 've', ',\”', '\’', 'll', '{',
		))
scored_raw = finder_raw.score_ngrams(bigram_measures.raw_freq)
bigrams_raw = finder_raw.nbest(bigram_measures.raw_freq, 50)

print("")
print(" ---------------------------------------------- ")
print("")
print("Callocations without filters (besides puncuation): ")
for pair in bigrams_raw:
	print(pair)










