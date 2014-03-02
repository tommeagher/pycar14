# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Introduction to basic Python types and methods
# 

# <markdowncell>

# Type each command in your interpreter exactly as I describe it. We're going to move very quickly here. Don't worry. We're going to repeat these ideas over and over in the other lessons. This is just to give you a quick overview of the very basics of programming in Python. If you have questions, don't keep them to yourself. Just ask.

# <markdowncell>

# #Strings

# <codecell>

variable = "nicar"

variable

# <markdowncell>

# In Python, you don't have to declare a variable before you assign a value to it. Just give it a name and assign it a value using the = sign.

# <codecell>

variable.upper()

# <markdowncell>

# .upper() is one of dozens of string method, in many ways similar to the functions you might be familiar with in Excel. What do you think this one does?

# <codecell>

variable

# <markdowncell>

# You might notice that the .upper() method doesn't permanently change the "variable" variable. We'll get to that in a minute.

# <codecell>

type(variable)

# <markdowncell>

# The built-in type function tells us what type of Python object our "variable" is. In this case, it's a string (or 'str'), which is a core type and brings with it a host of useful methods.

# <codecell>

dir(str)

# <markdowncell>

# This produces a list of all the methods that you can perform on a string (an object of the 'str' type), as well as other attributes and names associated with strings. For now, you can ignore the ones that start with a double underscore.

# <codecell>

variable[0:2]

# <markdowncell>

# This is called slicing, when you use the brackets to 'slice' out characters from a string based on their position. Notice in Python, that we start counting at zero. So variable[0] returns the "n" in "nicar". The value after the colon is the position that we stop before. So variable[0:2] returns all the characters from position 0 until before position 2.

# <codecell>

variable[0:2]="py"

# <markdowncell>

# Remember when the .upper() method didn't change the variable? A string is immutable. You can't change it in place, so if you want to change it, you have to create a new variable and assign the new value to it.

# <codecell>

variable.replace("ni","py")

# <codecell>

variable

# <markdowncell>

# See what I mean?

# <codecell>

newvariable = variable.replace("ni","py")

newvariable1=newvariable.upper()

newvariable1

# <markdowncell>

# Now let's use slicing to create a new string.

# <codecell>

newvariable2 = newvariable1[0] + newvariable1[1].lower() + newvariable1[2:]

# <markdowncell>

# _A hint if you're using iPython, start typing "newva" and hit the tab button. It remembers all the variables you've assigned in your session and offers autocomplete._

# <codecell>

newvariable2

# <codecell>

print newvariable2

# <markdowncell>

# If you know the name of the method you want to use, but don't remember its purpose, or the arguments you need to pass to it, try the help() function.

# <codecell>

help(newvariable2.lower)

# <markdowncell>

# Let's add the year to our string "pycar"

# <codecell>

ourclass = newvariable2 + 14

# <markdowncell>

# Oops. You can't concatenate an integer and a string. Let's make that 14 a string by wrapping it in quotes.

# <codecell>

ourclass = newvariable2 + "14"

# <codecell>

ourclass * 5

# <headingcell level=1>

# Ints

# <markdowncell>

# Strings are great, but we're data journalists. We like to deal in numbers. So let's take a quick look at integers.

# <codecell>

mynumber = 14

mynumber * 5

# <codecell>

type(mynumber)

# <codecell>

newnumber = mynumber + 84

newnumber

# <codecell>

newnumber += 500
newnumber

# <markdowncell>

# A useful shortcut, if you don't want to keep creating new variables, you can assign the new value to a variable of the same name using the += operator.

# <markdowncell>

# #Lists

# <markdowncell>

# One of my favorite Python types is the list. A list is an ordered collection of objects (variables, strings, integers, other lists, and more) and is mutable. You create a list by assigning wrapping it in brackets and assigning it to a variable. If you're familiar with JavaScript or Ruby, a Python list is very similar to an array.

# <codecell>

mylist = [ourclass, newnumber]

# <codecell>

myname = "Tom"

mylist.append(myname)

mylist

# <codecell>

yourname = "Heather"
yournumber = 37
ournumber = 18

mylist.append(yourname)
mylist.append(yournumber)
mylist.append(ournumber)

mylist

# <markdowncell>

# Because a list is a sequence (just as a string is a sequence of characters), we can also use the slicing method to pull out specific items from the list.

# <codecell>

mylist[0:1]

# <markdowncell>

# Probably the most powerful (and potentially dangerous) thing to do with a list is to iterate over it using a for loop, to perform some action on each item in the list.

# <codecell>

for item in mylist:
    print item * 5

# <markdowncell>

# One thing that trips up a lot of people when they first dabble in Python is its "meaningful whitespace." The way to tell the loop what actions to perform on each go-round, is to nest those actions underneath the "for" declaration. You nest the actions by indenting four spaces. You can technically also use tabs, but you can't mix spaces and tabs, and most Pythonistas prefer four spaces. This makes your loop more readable, but can occasionally make it easy to overlook when an action is incorrectly nested.
#     

# <markdowncell>

# #dicts

# <markdowncell>

# The last Python type we'll talk about right now is the dictionary. If you're familiar with an object in JavaScript or a hash in Ruby, a dictionary in Python is very similar. It's an object that stores an unordered series of keys and values. You can create one by using the curly brackets.

# <codecell>

mydict = {}

# <codecell>

mydict['class_size']=ournumber
mydict

# <codecell>

mydict['nerds']='at bar'

mydict

# <codecell>

mydict['nerds']

# <codecell>

mylist.append(mydict)
mylist

# <markdowncell>

# You can nest a dictionary inside a list, if it suits you.

# <codecell>

mylist[1:-1]

# <markdowncell>

# This barely skims the surface of what you can do in Python, but hopefully this overview will make you comfortable in starting the rest of the exercises or other tutorials.

# <codecell>

exit()

