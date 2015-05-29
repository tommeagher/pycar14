"""
variables
"""
# create an integer
my_integer = 25

# create a string
my_string = "We're going to learn Python at #NICAR15"

# create a list
my_list = [1, 2, 3]


"""
integers
"""
# print your integer
print my_integer

# get the type of your integer
print type(my_integer)

# do some addition
my_sum = my_integer + 10
print my_sum

# do some subtraction
my_difference = my_integer - 10
print my_difference

# do some multiplication
my_product = my_integer * 10
print my_product

# do some division
my_dividend = my_integer / 10
print my_dividend


"""
floats
"""
# create float, assign it a value and print it
my_float = 25.345
print my_float

# divide a float in half
print 23.46/2

# divide a number in half
print 5/2


"""
order of operations
"""
#create variable for a new value
new_value = 25.345

#create for an old value
old_value = 21.924

#calculcate percent change
percent_change = new_value - old_value / old_value
percent_change = (new_value - old_value) / old_value
percent_change = ((new_value - old_value) / old_value) * 100


"""
Strings
"""
# print your string
print my_string

# get the type
print type(my_string)

# get the length
print len(my_string)

# convert it to lowercase
print my_string.lower()

# convert it to uppercase
print my_string.upper()

# convert it to titlecase
print my_string.title()

# concatenate strings
print my_string + my_string

# split strings
print my_string.split("learn")

# join strings
print "+++".join([my_string, my_string])

# remove a character
print my_string.replace(" ", "##")

# strip whitespace
print "  this string has whitespace  ".strip()

# removes only leading whitespace chars
print "  this string has whitespace  ".lstrip()

# removes only trailing whitespace chars
print "  this string has whitespace  ".rstrip()


"""
Lists
"""
# create a list, you can use strings, intergers, etc
my_list = ["We're going to learn Python at #NICAR15", 10, 15, 20]

# print the list
print my_list

# print its type
print type(my_list)

# print its length
print len(my_list)

# create a list of numbers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print the first item in the list
print my_list[0]

# print the last item in the list
print my_list[-1]

#print all items from 4 through the end. We call this slicing.
print my_list[3:]

#print the items from the start to the penultimate
print my_list[:-1]

#print the middle 4 items
print my_list[3:-3]

# add an item to the list and see if it was added
my_list.append(11)
print my_list

# delete the last item in the list
del my_list[-1]
print my_list

# set the last value in the list to a variable
last = my_list.pop(-1)


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
print x == y
print x != y
print x > y
print x >= y
print x < y
print x <= y

# create two variables, assign one as a number and one as a string and compare them
x = 10
y = "10"
print x == y
print x != y
print x > y
print x >= y
print x < y
print x <= y

# for extra credit, try to compare lengths
print len(x) == len(y)
