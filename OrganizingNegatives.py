# sort out the output.txt negatives go 1st, non negatives 2nd
# new program to sort data read in that file
# type into terminal: python SearchNegatives.py <1950s_Government.txt >output.txt
# type into terminal: python OrganizingNegatives.py <1950s_Government.txt >output.txt
# July, 16 2020 * Sahara Palacios
###


     


import fileinput as fi
import re

# list1 = ['ingenting']
#def myKey(x):
  #patternList = ('ingenting', '[^ingenting')

negative_pattern = re.compile('ingenting')
non_negative_pattern = re.compile('[^ingenting]')
for line in fi.input():
    if negative_pattern.search(line):
    
        negative = []
        negative.append(line)
        first_negative = [0]
        print ('updated negative list: ', negative)
    else:
        nonnegative = []
        nonnegative.append(line)
        last_nonnegative = [-1]
        print ('updated nonnegative list:', nonnegative)
    
        