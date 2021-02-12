import re
import urllib.request

import bs4 as bs
import nltk

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
article = scrapped_data .read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text
#print(article_text)

#start pre-processing
# Cleaing the text
processed_article = article_text.lower()
processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )
processed_article = re.sub(r'\s+', ' ', processed_article)

# Preparing the dataset
#use nltk.sent_tokenize utility to convert our article into sentences.
all_sentences = nltk.sent_tokenize(processed_article)
#To convert sentences into words,  use nltk.word_tokenize utility.
all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# Removing Stop Words
#from nltk.corpus import stopwords
#for i in range(len(all_words)):
   # all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]

#Creating Word2Vec Model
from gensim.models import Word2Vec
word2vec = Word2Vec(all_words, min_count=2)
vocabulary = word2vec.wv.vocab
print(vocabulary)

v1 = word2vec.wv['artificial']
sim_words = word2vec.wv.most_similar('intelligence')
print(sim_words)