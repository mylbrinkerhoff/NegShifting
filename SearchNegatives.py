#
# Searching for Negatives
#
# July 15, 2020 * Sahara Palacios
#

import fileinput as fi
import re

negative_pattern = re.compile('ingenting')
non_negative_pattern = re.compile('[^ingenting]')

negative = []
nonnegative = []

for line in fi.input():
    line = line.rstrip()
    if negative_pattern.search(line):
        negative.append(line)
        # print ('updated negative list: ', negative)
     #if non_negative_pattern.search(line):
    else:
        nonnegative.append(line)
        # print ('updated nonnegative list: ', nonnegative)

print(negative)
print(nonnegative)
     
     