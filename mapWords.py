'''
Created on Oct 2, 2015

@author: benjamin
'''

from transformer import *
import collections
import re
# Read in short words and phoneme data base

with open('/home/benjamin/git/pirat/data/words_long.txt','r') as file:
    shortWords = file.readlines()

for i in range(len(shortWords)):
    shortWords[i] = shortWords[i].rstrip().upper()

with open('/home/benjamin/git/pirat/data/phonemeDB_clean.txt','r') as pfile:
    pdata = pfile.readlines()
    
words = []
phonemes = [] 
for i in range(len(pdata)):
    
    if ("'" in pdata[i]) | ('(' in pdata[i]) | ('.' in pdata[i]) : continue 
    tokens = pdata[i].split()
    words.append(tokens[0])
    phonemes.append(tokens[1:])
  
# find short words in db and get there phoneme representation 
        
idx = []  
for w in shortWords:
    idx.append(words.index(w))  

queries = []
usedWords = []
for i in range(len(idx)):
    if len(phonemes[idx[i]]) < 5:
        queries.append(phonemes[idx[i]])
        usedWords.append(shortWords[i]) 
        
        
# with open('/home/benjamin/git/pirat/data/words.txt','w') as wfile:
#     for item in usedWords:
#         print>>wfile, item
        

# match short word phonemes to db
tr = transformer()

qs = []
for i in range(len(queries)):
    qs.append(tr.transform(queries[i]))
ps = []
for i in range(len(phonemes)):
    ps.append(tr.transform(phonemes[i]))
    
    
matches = []
for i in range(len(ps)):
    # identifier short word | index in long word | length of short word
    m = []
    for j in range(len(qs)):
        if qs[j] in ps[i]:
            ind = [mi.start() for mi in re.finditer(qs[j], ps[i])][0]
            leng = len(qs[j])
            m.append([j,ind,leng])
            # substitute found match to prevent overlap matches
            ps[i] = tr.getSub(ps[i],qs[j])
    matches.append(m)


allMatches = []
for i in range(len(matches))  :
    if len(matches[i]) > 1:
        outString = ''
#         putIdx = []
#         skipList = []
#         putList = []    
#         for m in matches[i]:     
#             putIdx.append(m[0]) 
#             skipList.append(range(m[1],m[1]+m[2]))
#             putList.append(m[1])
#         skipList = set(skipList)
#         putList = set(putList)
#         for j in phonemes[i]:
#             if j in putList: outString = outString+'>'+usedWords[putIdx]
#             if j in skipList: continue     
#             outString = outString+'>'+phonemes[i][j]         
        fullString = words[i]+outString
        allMatches.append(fullString)

for match in allMatches:
    print(match)

print(len(allMatches))


