'''
Created on Oct 3, 2015

@author: benjamin
'''

import string

class transformer:
    

    def __init__(self):
        ids = []
        for i in range(10):
            ids.append(str(i))    
        alphabet = list(string.ascii_lowercase)
        for i in alphabet:
            ids.append(i)
        ids.append('.')
        ids.append(',')
        ids.append(':')
        ids.append(';')
        
        with open('/home/benjamin/git/pirat/data/phonemes.txt','r') as file:
            phonemes = file.readlines()
        for i in range(len(phonemes)):
            phonemes[i] = phonemes[i].rstrip()
        self.phonemes = phonemes
        self.ids = ids
    
    def transform(self,l):
        idx = []
        for i in l:
            idx.append(self.phonemes.index(i))
        outList = []
        for i in idx:
            outList.append(self.ids[i])
        return ''.join(outList)
    
    def getSub(self,p,q):
        # when you find a match, replace the found sequence
        # Insert unknown symbol ! to prevent matches within this match
        # allow overlap by leaving first and last phoneme
        first = q[0]
        last = q[-1:]
        sub = '!'
        for i in range(len(q)-1):
            sub = sub + '!'
        #p = p.replace(q,first+sub+last)
        p = p.replace(q,sub)
        return p
        


        