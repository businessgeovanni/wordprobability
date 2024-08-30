from nltk.corpus import brown
import nltk
#sets news_text to brown corpus from news category
news_text = brown.words(categories='news')
#tokenizing lowercase letters / words
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']

#if its a new word, puts it into the array
for w in news_text:
    if w.lower() not in modals:
        modals.append(w.lower())

#prints the words total count, and a probability of it occuring in the corpus
for m in modals:
    if fdist[m] > 50:
        print(m + ' is a complete and correct word as per corpus',  fdist[m], ', and its probability is' , fdist[m]/len(fdist))
        

