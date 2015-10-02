'''
Created on Oct 2, 2015

@author: benjamin
'''
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
        
idx = []  
for w in shortWords:
    idx.append(words.index(w))  

queries = []
usedWords = []
for i in range(len(idx)):
    if len(phonemes[idx[i]]) < 5:
        queries.append(phonemes[idx[i]])
        usedWords.append(shortWords[i]) 
        
        
with open('/home/benjamin/git/pirat/data/words.txt','w') as wfile:
    for item in usedWords:
        print>>wfile, item
        
        
# xqs = []
# for i in range(queries):
#     transform(queries[i])
#     
# for i in range(1000):
#     l = phonemes[i]
#     for j in range(len(queries)):
#         
#     
# 
# 
# def transform:
    







print('lala')


