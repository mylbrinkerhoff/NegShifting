#
# Counting lines
# 
# Wednesday 15, 2020 * Sahara Palacios
#
#

import fileinput as fi

#variables?
count = 0 

#counting the number of lines in the file
for line in fi.input():
    count = count + 1 
    

#printing the count of the lines
print('The number of lines in the text is {count}'.format(count = count))