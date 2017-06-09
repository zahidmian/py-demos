import nltk 
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import sys, os
#import pickle
#import os

LONG_WORD_LEN = 12 # word length considered long and dumped to file for review
NUM_OF_TOPICS = 5  # number of topic to produce for LDA
NUM_OF_PASSES = 5 # number of passes for LDA model
NUM_OF_WORDS = 6   # number of words to include in each topic 

df = pd.read_csv('pubmed-oa-subset.csv',  encoding = "ISO-8859-1")

# create English stop words list
en_stop = stopwords.words('english') + ['.', '''''', '-', ':', ',', '(', ')', '[', ']']

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
dictionary = corpus = ldamodel = None

doc_set = df.iloc[:,3].str.lower().tolist()

def process_text(doc_set = []):
    global dictionary, corpus, ldamodel
    lemmatized_tokens = None
    texts = []
    
    for i in doc_set:        
        raw = i
        #tokens = word_tokenize(raw.decode('utf-8'))
        try:
            tokens = word_tokenize(raw)
        
            # remove stop words
            stopped_tokens = [i for i in tokens if not i in en_stop]
        
            '''
            # stem tokens        
            filename = "sr_stem_freq_dist.txt"
            #stemmed_tokens = [p_stemmer.stem(item.decode('utf-8')) for item in stopped_tokens]
            stemmed_tokens = [p_stemmer.stem(item) for item in stopped_tokens]
            #add tokens to list
            texts.append(stemmed_tokens)        
            '''
        
            # lemmatize tokens
#            filename = "sr_lemm_freq_dist.txt"
            lemmatizer = WordNetLemmatizer()
            lemmatized_tokens = [lemmatizer.lemmatize(item) for item in stopped_tokens]
            #add tokens to list
            texts.append(lemmatized_tokens)
        except Exception as e:
            #print (RuntimeError)
            #exc_type, exc_obj, exc_tb = sys.exc_info()
            #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            #print(exc_type, fname, exc_tb.tb_lineno)
            pass
        
        
    
    # determine avg number of words by summary
    # this isn't necessary ... just divide total words by total documents
    #count_of_words = [len(x) for x in texts]
    #print 'avg words/entry: ' + str(reduce(lambda x,y: x+y, count_of_words)/len(count_of_words))
    
    # save distribution to file    
    reduced_list = [item for sub in texts for item in sub]
    fdist = nltk.FreqDist(reduced_list)
#    save_to_file(filename, fdist)
    
    # turn tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)

    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_OF_TOPICS, id2word = dictionary, passes=NUM_OF_PASSES)
    
    print ('avg words/entry: {:4.2f}'.format( len(reduced_list) / float(len(doc_set))))
    fdist = nltk.FreqDist([len(w) for w in reduced_list])
#    save_to_file('freq_dist_len_of_words.txt', fdist)
    
    long_words = [w for w in reduced_list if len(w) >= LONG_WORD_LEN]
#    save_to_file('long_words.txt', long_words)
    
    #fdist.plot(cumulative=False)  #with open("l")

'''    
def save_dist(filename, dist = {}):
    with open(filename, "wb") as f:
        for (k,v) in dist.items():
            f.write(k.encode('utf-8') + ', ' + str(v) + '\n')

def save_list(filename, tokens = []):
    with open(filename, "wb") as f:
        [f.write(tok) for tok in tokens]
'''

#def save_to_file(filename, tokens):
#    pfile = os.path.splitext(filename)[0]+'.p'
#    #print 'filename: {}, pfile: {}'.format(filename, pfile)
#    pickle.dump(tokens, open(pfile, "wb") )
#    
#    if type(tokens) is list:
#        with open(filename, "wb") as f:
#            [f.write(tok.encode('utf-8') + '\n') for tok in tokens]
#    elif type(tokens) is dict or type(tokens) is nltk.probability.FreqDist:
#        with open(filename, "wb") as f:
#            for (k,v) in tokens.items():
#                try:
#                    if k.isnumeric():
#                        f.write(str(k).encode('utf-8') + ', ' + str(v) + '\n')
#                    else:
#                        f.write(k.encode('utf-8') + ', ' + str(v) + '\n')
#                except:                    
#                    None

for t in range(1, 3):            
    print ('Trial {}'.format(t))
    process_text(doc_set)

    #print(ldamodel.print_topics(num_topics=NUM_OF_TOPICS, num_words=4))
    lda = ldamodel.print_topics(num_topics=NUM_OF_TOPICS, num_words=NUM_OF_WORDS)
    for i in range(0, len(lda)):
        print (lda[i])    

    print ('\n')
