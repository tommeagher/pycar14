Project #1
==========

**9:30 - 10:45 a.m.**

What is a [number](https://docs.python.org/2/tutorial/introduction.html#numbers)? What is a [string](https://docs.python.org/2/tutorial/introduction.html#strings)? What is a [list](https://docs.python.org/2/tutorial/introduction.html#lists)?

Nevermind that, what's a [Python](https://docs.python.org/2.7/)?

Python is a programming language. It was created around 1991 by an individual named [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum).

You may hear others call Python a [scripting language](https://en.wikipedia.org/wiki/Scripting_language). You may also hear it called an interpretative language. In essence these are interchangeable terms. In Python you write programs that are interpreted line by line. These programs - or scripts - automate tasks that would otherwise be completed one by one.

One feature of Python that takes some getting used to is its use of whitespace and indentation. One to remember this is to think of creating an outline. You have main bullet points and you might have an item indented beneath that relates to something above it.

The Python interpreter can be accessed through the command line (terminal, shell, etc). On a Unix-based (Mac OS) or Linux machine - which come with Python installed by default - you enter the Python interpreter by typing ```python``` followed by the return key. On a Windows machine, things are a bit more cumbersome.

Let's start by looking at some key components of any programming language - variables, strings, numbers and comparisons. All of this is contained within the [official Python tutorial](https://docs.python.org/2/tutorial/introduction.html#) to the standard library. We'll consider Python lists as a containter that we can fill and we'll work toward using a couple core libraries - ```urllib``` and ```csv```  - to download a csv file and read the contents.

**The files**

* ```_1_getting_started.py``` and ```_1_getting_started_complete.py```

    * Indentation

    * Comments

    * Variables
        * A backbone of any programming language
        * Variables have a scope
        * Variables have a value
            * Can be None, could be True or False
            * Or it could be something else... a number or a string
        * format is always 'variable equals value'

    * [Numbers](https://docs.python.org/2/tutorial/introduction.html#numbers)
        * Whole numbers have a type and that type is integer
        * Fractions have a type and that type is float
        * Learning about numbers
            * get the [type](https://docs.python.org/2/library/functions.html#type)
            * addition
            * subtraction
            * multiplication
            * division
                * import future
            * order of operations

    * [Strings](https://docs.python.org/2/tutorial/introduction.html#strings)
        * Generally, synonymous with words.
        * You can use double quotes or single quotes to create strings
        * If using single quotes, apostrophes and single quotes within string must be escaped
        * [Unicode strings](http://www.unicode.org/) - Mention & explain?
        * Learning about numbers
            * double quotes vs. single quotes
            * get its type
            * get its length
            * [lowercase](https://docs.python.org/2/library/stdtypes.html?highlight=strip#str.lower)
            * [uppercase](https://docs.python.org/2/library/stdtypes.html?highlight=strip#str.upper)
            * [titlecase](https://docs.python.org/2/library/stdtypes.html?highlight=strip#str.title)
            * [split](https://docs.python.org/2/library/stdtypes.html?highlight=strip#str.split)
            * join
            * [replace a character](https://docs.python.org/2/library/stdtypes.html?highlight=strip#str.replace)
            * strip whitespace
                * [all](https://docs.python.org/2/library/stdtypes.html?highlight=strip#str.strip)
                * [leading whitespace](https://docs.python.org/2/library/stdtypes.html?highlight=strip#str.lstrip)
                * [trailing whitespace](https://docs.python.org/2/library/stdtypes.html?highlight=strip#str.rstrip)

    * [Lists](https://docs.python.org/2/tutorial/introduction.html#lists)
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

    * Comparisons and Conditionals

        * [Comparisons](https://docs.python.org/2/library/stdtypes.html#comparisons)
            * equals
            * not equals
            * greater than
            * greater than equal to
            * less than
            * less than equal to

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

        * Conditionals
            [if/elif/else](https://docs.python.org/2/tutorial/controlflow.html#if-statements)
            [for](https://docs.python.org/2/tutorial/controlflow.html#for-statements) 

* ```_2_download_and_read.py``` and ```_2_download_and_read_complete.py```
    * Now that we have some concepts, let's write a program already
        * Downloading a csv file
        * Open it
        * Loop through each row and print the data

* ```_3_extra_credit.py``` and ```_3_extra_credit_complete.py```
    * We know how to download a csv file and read its contents. Let's see if we can search the output for a specific value
