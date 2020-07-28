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


# age = input("What is your age? ")
# age = int(age)
# if age < 16:
#     print("You are to young to drive in Utah!")
# elif age >= 70:
#     print("You should probably not drive anymore.")
# elif age == 16:
#     print("You can now drive in Utah!")
# elif age > 16:
#     print("You can drive in Utah!")
# else:
#     print("You didn't give me an age!")

# bikes = ['trek', 'redline', 'giant']
# print(bikes)

# for bike in bikes:
#     print(bike)