# Questão 3

# Conforme pedido, foi criado uma biblioteca com várias funções

import string
import re
from collections import Counter

def cleanword(st):
    word = "".join(re.findall("[a-zA-Z]+", st))
    return(word)

def has_dashdash(st):
    if(re.search('-', st)):
        return (1)
    else:
        return 0

def extract_words(st):
    word = re.split(r'\s',st)
    return(word)

def wordcount(st, word):
    count = st.count(word)
    return(count)

def longestword(word_list):  
    word_list = re.split(r'\s',word_list)
    longest =  max(word_list, key=len)
    length = len(longest)
    return length

def wordset(s):
    c = Counter(s.split(' '))
    return set(k for k,v in c.items() if v==1)    

if __name__ == "__main__":

    cleanword()
    has_dashdash()
    wordset()
    longestword()
    wordcount()
    extract_words()