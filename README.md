# Collocations in Children's Books
The project collected the most common pairs of words, or collocations, found in a corpus of children’s books. 

## Motivation
The purpose of this project is to understand how children learn collocations by seeing the various types of collocations that children are being exposed to in the books that they read. Children are constantly expanding their vocabulary and learning how to use newly-learned words correctly. Teachers and other educators can then use the information to reinforce the collocations that children are exposed to in the books, or to introduce new collocations that aren’t seen as often in the books that are important for children to learn. They can potentially also use the results to suggest reading recommendations to children.

## Corpus
The books that were used to build the corpus were taken from [Project Gutenberg - Category: Children's Bookshelf](https://www.gutenberg.org/wiki/Children%27s_History_(Bookshelf)/). The corpus that was built consisted of 362 books and a total of 76,294,882 words. The books that were used can be found in the excel file “child_corpora_book_list.xlsx” and the full text of all the books in the corpus can be found in the file "combined_text.txt".

## Results
We hypothesized that the most common type of collocation would be an adjective + noun pair such as "old man" or "blue sky", but the most common type was an adverb + verb pair (i.e. "will be" or "have been"). Even with some filters, results were not too meaningful due to the large number of common, simple collocations in the English language.

### Possible Future Extensions
* To produce better results for the hypothesis of this project, the project could have incorporated parts-of-speech tagging. The code can include a method to automatically tag the parts of speech for each of the collocations. Then a filter would be placed to specifically parse out syntactic bigrams such as adjective-noun or verb-noun. This extension of the project would probably have produced more meaningful results.

* Another extension could be to mimic the same procedures in finding the collocations and applying it onto the CHILDES corpora. It may be interesting to see how collocation applies to children’s dialogue, as compare results to the children’s book corpora. Analysis of the data can possibly be used to see if children are learning new collocations from the books they read and can benefit from being exposed to different difficulties of text. 

## Authors
Huynh Hoang, Nancy Nguyen
