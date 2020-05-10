import string
import re
from collections import Counter

st = "?+='w-o-r-d!,@$()"
st1 = 'what?'
st2 = "'now!'"
word = "".join(re.findall("[a-zA-Z]+", st))
word1 = "".join(re.findall("[a-zA-Z]+", st1))
word2 = "".join(re.findall("[a-zA-Z]+", st2))
print(word)
print(word1)
print(word2)

st = "'now!'"

test = re.split(r'\s','eu te amo muito baby husky husky')
print(test)
print(test.count("husky"))


sent = 'this is my sentence string this is also my test string'

def wordset(s):
    c = Counter(s.split(' '))
    return set(k for k,v in c.items() if v==1)

print(wordset(sent))
# returns:

def longestword(word_list):  
    word_list = re.split(r'\s',word_list)
    longest =  max(word_list, key=len)
    length = len(longest)
    print(len(longest))
    print(word_list)
    return length

test = 'eu te amo muito baby husky husky'
longestword(test)