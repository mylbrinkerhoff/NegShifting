#
# Searching for Negatives
#
# July 15, 2020 * Sahara Palacios
#

import fileinput as fi
import re

negative_pattern = re.compile('ingenting')
non_negative_pattern = re.compile('[^ingenting]')
for line in fi.input():
    if negative_pattern.search(line):
    
        negative = []
        negative.append(line)
        print ('updated negative list: ', negative)
     #if non_negative_pattern.search(line):
    else:
        nonnegative = []
        nonnegative.append(line)
        print ('updated nonnegative list: ', nonnegative)


     
     