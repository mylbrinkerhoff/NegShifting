# -*- coding: utf-8 -*-

#####
# This code is based on the code written by my intern during the SIP program at UCSC
# I have renamed it FindNIs.py and have included the original description in this forematter. 
# There are a few minor changes that I have made to this code to make it run smoother.
# --MLB
# 
# # Search.Fiction.py
# # make a script that will search for the forms (ingen, inga, inget) while ingoring the other words
# #
# # I needs to be sorted into two groups! pronouns and determiners:
# # (ingen = det) (ingenting = pronouns).
# #
# # Looking for something like "ingenting..pn" or "ingen..pn"
# # May need to specify if there's a noun following "ingen" and separate them
# #
# # Sahara Palacios * started: July 18, 2020 * 
#
# FindNIs.py
# 
# 
# This script will search through a output text from the Swedish Cultronomics Gigaword Corpus
# which has POS tagging. It will search through the file line by line and search for NI prononouns.
# It organizes the lines into lists for each type of NIPs that I am concerned about and then print each
# of the lists for further annotation into an output file entered into the command line.
# 
# 
# Myke Brinkerhoff * Santa Cruz, CA * 2020 Sept 30 (W)
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