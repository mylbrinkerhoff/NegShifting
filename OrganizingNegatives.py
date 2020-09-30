# sort out the output.txt negatives go 1st, non negatives 2nd
#
# new program to sort data read in that file and sort it!
#
# OrganizingNegatives.py
# 
# type into terminal: python OrganizingNegatives.py
#
# July, 16 2020 * Sahara Palacios
###


     

#give the path to output
filename = ("/Users/SaharaPalacios/repo/Data_Sets/output.txt")

#open file one line at a time and then sort it
#change the path to whatever is best for your computer
with open(filename) as file_object:
  lines = file_object.readlines()
  lines.sort()

#print out the file that has been sorted 
for line in lines:
  print(line)

 #   if negative_pattern.search(line):
 #   
#    negative = []
#      negative.append(line)
#   
#    first_negative = [0]
 #      print ('updated negative list: ', negative)
  # else:
   #    nonnegative = []
    #   nonnegative.append(line)
     #  last_nonnegative = [-1]
      # print ('updated nonnegative list:', nonnegative)
    
        
