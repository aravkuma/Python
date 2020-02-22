#!/usr/bin/env python
# coding: utf-8

# In[130]:


import string
import collections
import re
import matplotlib.pyplot as plt
from collections import Counter
from string import punctuation
from operator import itemgetter
import math, string, sys, fileinput
import sys

class Reader:
    def __init__(self, file, dict):
        self.file = file
        self.dict = {}
    
    def create_dict(self):
        with open ('C:\\Users\\aravi\\Desktop\\Python\\Python Subject\\text1','r') as f:
            file = f.read()
            file = file.lower()
            cleanText = re.sub('[^A-Za-z0-9]+', '', file)
            count = dict(collections.Counter(cleanText))
            #del count[' ']
            #del count['\n']
            #print(count)
            return count

    
            
r=Reader('C:\\Users\\aravi\\Desktop\\Python\\Python Subject\\text1','')
#r.create_dict()


class Decipher(Reader):
    def __init__(self, path1, path2, chosenstr):
        super().__init__(path1, '')
        self.path1 = 'C:\\Users\\aravi\\Desktop\\Python\\Python Subject\\text1'
        self.path2 = 'C:\\Users\\aravi\\Desktop\\Python\\Python Subject\\text2'
        chosenstr = {}
        with open ('C:\\Users\\aravi\\Desktop\\Python\\Python Subject\\text2','r') as c:
            coded = c.read()
        self.hist = []
#ordered = []
#deciphed = {}
#self.format = {}

    def outputreader(self):
        outputreader = super().create_dict()
        #print(outputreader)
        return outputreader

    def create_hist(self):
        hist = super().create_dict()
        print("Output of dictionary is")
        print(hist)
        print("Output of the frequency of each letter in alphabetical order is")
        print(sorted(hist))
        self.hist = hist

    def plot_pie(self):
        print("Pie Chart")
        labels = self.hist
        sizes = super().create_dict()
        explode = (0, 0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        plt.pie(sizes.values(), explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        plt.show()
        

    def plot_hist(self):
        print("\nHistogram")
        hist1 = super().create_dict()
        plt.hist(hist1.values(), bins = 10)
        plt.show()


    def create_ordered(self):
        
        outputreader1 = self.outputreader()
        freq = {} 
        b=dict(outputreader1)
        sort_b = sorted(b.items(), key=lambda pair: pair[1], reverse=True)
        self.ordered = [x[0] for x in sort_b]
        print("Letter in the alphabet by the order of frequency")
        print(self.ordered)       
        
    
    def decipher(self):
        self.deciphed = ''
        
        with open ('C:\\Users\\aravi\\Desktop\\Python\\Python Subject\\text2') as r:
            fcontent = r.read()
            print("\nThe original content in the text2\n",fcontent)
            s = ord('z') - ord('e')
         
            # traverse text 
            for i in range(len(fcontent)):
                char = fcontent[i].lower()
                decrypt_ch = chr((ord(char) - s - 97) % 26 + 97) 
                self.deciphed += decrypt_ch.upper() if fcontent[i].isupper() else decrypt_ch
                    
            print("\nThe deciphed content of the text2\n", self.deciphed)
        return self.deciphed
    

    def compute_entropy(self):
        
        def range_bytes (): return range(256)
        def range_printable(): return (ord(c) for c in string.printable)
        def H(data, iterator=range_bytes):
            if not data:
                return 0
            entropy = 0
            for x in iterator():
                p_x = float(data.count(chr(x)))/len(data)
                if p_x > 0:
                    entropy += - p_x*math.log(p_x, 2)
            return entropy

        def main ():
            for row in fileinput.input():
                string = row.rstrip('\n')
                print ("%s: %f" % (string, H(string, range_printable)))

        for str in ['C:\\Users\\aravi\\Desktop\\Python\\Python Subject\\text1']:
            print("\nEntropy output\n")
            print ("%s: %f" % (str, H(str, range_printable)))

    def write_code(self):
        
        print("\nThe output of this file is stored in the location \n 'C:\\Users\\aravi\\Desktop\\Python\\Python Subject\\Deciphedoutput.txt' as a text file")
        formatdecipher = self.deciphed
        file = open ("C:\\Users\\aravi\\Desktop\\Python\\Python Subject\\Deciphedoutput.txt","w")
        file.write(formatdecipher)
        file.close()
        

d=Decipher('C:\\Users\\aravi\\Desktop\\Python\\Python Subject\\text1','','')
d.create_hist()
d.plot_hist()
d.plot_pie()
d.create_ordered()
d.compute_entropy()
d.decipher()
d.write_code()


# In[ ]:





# In[ ]:




