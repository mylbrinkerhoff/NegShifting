# alphabet = 'αβγδεζηθικλμνξοπρςστυφχψ'
# print(alphabet)

filename = 'test.txt'

# Reading an entire file at once'
with open(filename) as f_obj:
    contents = f_obj.read()

# Reading line by line
# with open(filename) as f_obj:
#     for line in f_obj:
#         print(line.rstrip())

# Opening the file one line at a time
# with open(filename) as f_obj:
#     lines = f_obj.readlines()

# for line in lines:
#     print(line.rstrip())

# Testing lists
# squares = []
# for x in range(1,11):
#     squares.append(x**2)

# print(squares)

# Writing to an output
output = 'output.txt'

with open(output, 'w') as f:
    f.write(contents.rstrip())