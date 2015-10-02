'''
Created on Oct 2, 2015

@author: benjamin
'''

from transformer import *

# Read in short words and phoneme data base

with open('/home/benjamin/git/pirat/data/words_long.txt','r') as file:
    shortWords = file.readlines()

for i in range(len(shortWords)):
    shortWords[i] = shortWords[i].rstrip().upper()

with open('/home/benjamin/git/pirat/data/phonemeDB.txt','r') as pfile:
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
for i in range(1000):
    m = []
    for j in range(len(qs)):
        if qs[j] in ps[i]:
            m.append(j)
    matches.append(m)


#for i in range(len(matches))            
         
     
 
 







print('lala')


