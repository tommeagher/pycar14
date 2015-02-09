"""
* Indentation
"""


"""
* Comments
"""


"""
* Variables
    * A backbone of any programming language
    * Variables have a scope
    * Variables have a value
        * Can be None, could be True or False
        * Or it could be something else... a number or a string
"""

#format is always 'variable equals value'
my_integer = 25
my_string = "This variable is a string"
my_list = [1,2,3]


"""
* Numbers
    * Whole numbers have a type and that type is integer
    * Fractions have a type and that type is float
"""

# integers
my_integer = 25
print my_integer

# get type
my_type = type(my_integer)
print my_type

# addition
my_sum = my_integer + 10
print my_sum

# subtraction
my_difference = my_integer - 10
print my_difference

# multiply
my_product = my_integer * 10
print my_product

# division
my_dividend = my_integer / 10
print my_dividend



# floats
# 23.46/2 >> 11.73
# 5/2 >> 2

# import future

my_float = 25.345
print my_float

my_total = my_integer + my_float
print my_total

# order of operations
# used when we want to determine percent change right?
# (new - old) / old

percent_change = 25.345 - 21.924 / 21.924
percent_change = (25.345 - 21.924) / 21.924
percent_change = ((25.345 - 21.924) / 21.924) * 100






"""
* Strings
    * You can use double quotes or single quotes to create strings
    * If using single quotes, apostrophes and single quotes within string must be escaped
    * [Unicode strings](http://www.unicode.org/) - Mention & explain?
"""

# strings
my_string = "We're going to learn Python at #NICAR15"
print my_string

# double quotes
double_quotes_string = "We're going to learn Python at #NICAR15"
print double_quotes_string

# single quotes
single_quotes_string = "We're going to learn Python at #NICAR15"
print single_quotes_string

# get type
print type(my_string)

# get length
print len(my_string)

# lowercase
print my_string.lower()

# uppercase
print my_string.upper()

# titlecase
print my_string.title()

# concatenate
print my_string + my_string

# split
print my_string.split("learn")

# join
print "+".join([my_string, my_string])

# remove a character
print my_string.replace(" ", "##")

# strip whitespace
print "  this string has whitespace  ".strip()

# removes only leading whitespace chars
print "  this string has whitespace  ".lstrip()

# removes only trailing whitespace chars
print "  this string has whitespace  ".rstrip()

"""
* Lists
    * We learned that integers and strings are data types
        * Python has something it calls a compound data type
        * These are container that can be used to group values together
    * The list is kind of like a five-gallon bucket with a couple important features
        * A list is sortable and a list has an index
            * Index starts at 0
            * Allows
        * A list is [mutable](https://docs.python.org/2/glossary.html#term-mutable), which means you can add and remove content
            * Can add and remove items from specfic indexes
        * Lists might contain items of different types, but usually the items all have the same type.
"""

my_list = ["We're going to learn Python at #NICAR15", 10]
print my_list
print len(my_list)
print type(my_list)




my_list = [1,2,3,4,5,6,7,8,9,10]

print my_list[0]
print my_list[-1]
print my_list.append(11)

# pop() returns the element you want to remove. del just deletes is
# pop is also useful to remove and keep an item from a list. Where del actually trashes the item.
# By default, pop without any arguments removes the last item:
a.pop()
del a[-1]


"""
* Comparisons and Conditionals
"""


# operators and comparisons
# https://docs.python.org/2/library/stdtypes.html
x = 5
y = 15
print x > y
print x >= y
print x < y
print x <= y

foo = 10
bar = "10"

print foo == bar
print foo != bar
print foo == int(bar)

print bar == foo
print bar != foo
print bar == str(foo)

foo = "2"
print len(foo) == len(bar)