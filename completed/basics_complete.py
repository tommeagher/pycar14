"""
Strings
"""
# create a string and assign it to a variable
my_string = "We're going to learn Python at #NICAR16"

# print your string. If you're using the interactive interpretor
# (rather than running this script from a saved file), you don't need to type "print"
print my_string

# get the type
type(my_string)

# get the length
len(my_string)

# remember that a string is just a series of characters, not a word or a sentence
# so you can "slice" off pieces of a string based on the index of the characters in it.
# Try to slice off the last 5 characters in my_string
my_string[-5:]

# convert it to lowercase
my_string.lower()

# convert it to uppercase
my_string.upper()

# convert it to titlecase
my_string.title()

# concatenate strings
my_string + my_string

# split strings
my_string.split("learn")

# join a list of strings
"+++".join([my_string, my_string])

# remove a character
my_string.replace(" ", "##")

# strip whitespace
"  this string has whitespace  ".strip()

# removes only leading whitespace chars
"  this string has whitespace  ".lstrip()

# removes only trailing whitespace chars
"  this string has whitespace  ".rstrip()

# I need help remembering what methods my variable has available
dir(my_string)

# I need help on a specific method
help(my_string.lower)


"""
integers
"""
# create an integer
my_integer = 25

# print your integer
print my_integer

# get the type of your integer
type(my_integer)

# do some addition
my_sum = my_integer + 10
print my_sum

# do some subtraction
my_difference = my_integer - 10
my_difference

# do some multiplication
my_product = my_integer * 10
my_product

# do some division
my_dividend = my_integer / 10
my_dividend

"""
floats
"""
# create float, assign it a value and print it
my_float = 25.345
print my_float

# divide a float in half
23.46/2

# divide a number in half
5/2


"""
Lists
"""
# create a list
a_list = [1, 2, 3]

# create a list, you can use strings, intergers, variables, etc
my_list = ["We're going to learn Python at #NICAR16", 10, 15, 20]

# print the list
print my_list

# print its type
type(my_list)

# print its length
len(my_list)

# create a list of numbers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print the first item in the list
my_list[0]

# print the last item in the list
my_list[-1]

#print all items from 4 through the end. We call this slicing.
my_list[3:]

#print the items from the start to the penultimate
my_list[:-1]

#print the middle 4 items
my_list[3:-3]

# add an item to the list and see if it was added
my_list.append(11)
my_list

# delete the last item in the list
del my_list[-1]
my_list

# set the last value in the list to a variable
last = my_list.pop(-1)
last
my_list

"""
Dictionaries
"""
# create an empty dictionary
mydict = {}

# add a key called "class_size", whose value is my_product
mydict['class_size']=my_product
mydict

# add a dictionary key called "nerds" and a value of "at bar"
mydict['nerds']='at bar'
mydict

# call the value of a dictionary for the key "nerds"
mydict['nerds']

"""
Conditionals & Comparisons
"""
# take your list or make a new one, loop through it printing out each value
my_list = [1, 2, 3, 4, 5, 6]
for x in my_list:
    print x

# create two variables, assign values and compare them
x = 5
y = 15
x == y
x != y
x > y
x >= y
x < y
x <= y

# create two variables, assign one as a number and one as a string and compare them
z = 10
v = "10"
z == v

# if x is greater than y, print my_list
# otherwise, print my_dict
if x > y:
	for z in my_list:
		print z
else:
	for whatever in my_list[-3:]:
		print whatever

# This barely skims the surface of what you can do in Python, 
# but hopefully this overview will make you comfortable enough to get started.
# exit the program
exit()