#########################################################
# 
# OrganizingNegative.py
# 
# Read in the lines of a file and then sort it 
#
# M. Brinkerhoff * SIP2020, UCSC * 2020 July 17 (F)
# 
#########################################################

# Give the path to the file
# Change the path to whatever is best for your computer
filename = ("/Users/mykelbrinkerhoff/repo/Data_Sets/output.txt") 

# Open file one line at a time and then sort it
with open(filename) as file_object:
  lines = file_object.readlines()
  lines.sort()

# Print out the file that has been sorted.
for line in lines:
  print(line)