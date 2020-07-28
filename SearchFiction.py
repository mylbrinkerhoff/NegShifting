# -*- coding: utf-8 -*-

#####
# Search.Fiction.py
# make a script that will search for the forms (ingen, inga, inget) while ingoring the other words
#
# I needs to be sorted into two groups! pronouns and determiners:
# (ingen = det) (ingenting = pronouns).
#
# Looking for something like "ingenting..pn" or "ingen..pn"
# May need to specify if there's a noun following "ingen" and separate them
# 
#  Sahara Palacios * started: July 18, 2020 * 
#####


import fileinput as fi
import re

output = "Fiction_Output.txt"

ingenting_pattern = re.compile('ingenting\.\.pn')
ingen_pattern = re.compile('ingen\.\.pn') #or re.compile('ingen..n')
#inga_pattern = re.compile('inga')
determiner_pattern = re.compile('ingen\.\.pn\.\d\s\w+\.\.nn') #vara..vb.1 den..pn.1 ingen..pn.1 tvekan..nn.1 om..pp.1 .
 #something similar to: ‘ingen..pn.\d\s\w+..nn’ mykel's guess *check regex cheat sheet

ingenting = []
ingen = []
determiner = []
pronoun = []
#with open(output, 'w') as f: 
for line in fi.input():
    line = line.strip()
    if ingenting_pattern.search(line):
        ingenting.append(line)
    elif ingen_pattern.search(line):
        ingen.append(line)
        #print ('updated ingenting list: ', ingenting)
     #else: 
     #    print('[^ingenting] [^ingen]')
    
for target_list in ingen:
    if determiner_pattern.search(target_list):
        determiner.append(target_list)
    else:
        pronoun.append(target_list)
#print each of the elements
print("___ingenting___")
for item in ingenting:
    print(item)
print("___pronoun___")
for item in pronoun:
    print(item)
print("___determiner___")
for item in determiner:
    print(item)

#print(ingenting)
#print(ingen)