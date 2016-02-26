#here i assume that word is a sequence of letters surrounded by spaces
import re
import collections
def count_words(text):
    output = dict()
    for x in text.lower().split(): 
        if output.has_key(x) == False:
            output[x] = 1
        else:
            output[x] += 1
    return output  

def average_wordcount(text):
    sentences = text.replace(',', ' ').replace('!', '.').replace('?', '.').split('.')
    word_count = 0 
    sentence_count = text.count('.')
    for x in sentences:
        word_count += len(x.split())
    return word_count / float(sentence_count)

def median_wordcount(text):
    sentences = text.replace('!', '.').replace('?', '.').split('.')
    del(sentences[-1]) 
    words_in_each_sentence = []
    for x in sentences:
        words_in_each_sentence.append(len(x.split()))
    words_in_each_sentence.sort()
    if len(words_in_each_sentence) % 2 == 0:
        return words_in_each_sentence[len(words_in_each_sentence) / 2 - 1] #if even return one closer to [0]  
    else:
        return words_in_each_sentence[len(words_in_each_sentence) / 2]

def ngrams(word, n):
    """return list of n-grams of the word"""
    letters = list(word)
    output = []
    for x in range(len(word) - n + 1):
        output.append(word[x:x+n])
    return output

def count_ngrams(text, n):
    """return dict with k=n-grams & v=number of this n-gram, 
    or false if no n-grams found"""
    output = dict()
    text = text.lower().split()
    all_ngrams = []
    for x in text:
        re.sub("[^a-zA-Z]+", "", x)
    for x in text:
        all_ngrams.extend(ngrams(x, n))
    for x in all_ngrams:
        if output.has_key(x) == False:
            output[x] = 1
        else: 
            output[x] += 1
    else:
        return output

def top_ngrams(text, n, number):
    """count [n]-grams in text and return list of pairs of top-[number] most frequent ones and their counts"""
    n_grams = count_ngrams(text, n)
    if count_ngrams(text, n) == False:
        return "No {}-grams found!".format(n)
    n_grams = sorted(n_grams.items(), key = lambda t: t[1], reverse = True)
    for x in range(0, len(n_grams) - number):
        n_grams.pop()
    return n_grams
