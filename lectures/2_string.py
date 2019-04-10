# Introduction to Python str object

single_quote = 'Single quote allow you to embed "double" quotes in your string.'
double_quote = "Double quote allow you to embed 'single' quotes in your string."
triple_quote = """Triple quotes allows to embed "double quotes" as well as 'single quotes' in
your string. And can also span across multiple lines."""

print(ord('a'))
print(ord('b'))
print(chr(99))


# The + operator concatenates strings.
# It returns a string consisting of the operands joined together.

a = 'hello'
b = ' '
c = 'people'
print(a + b + c)

# The * operator creates multiple copies of a string. If s is a string and n is an integer,
# either of the following expressions returns a string consisting of n concatenated copies of s.

a = 'hi'
n = 5
print(a * n)

a = '|hi|'
n = 3
print(n * a)

a = '|hi|'
n = -3
print('result=', n * a)

# bool operator on strings
# empty string is False in python

empty_string = ''
print(bool(empty_string))

non_empty_string = 'non_empty'
print(bool(non_empty_string))

# The in operator returns True if the first operand is contained within the second, and False
# otherwise:
s = 'foo'
print(s in 'That\'s food for thought.')
print(s in 'That\'s good for now.')

print('z' not in 'abc')
print('z' not in 'xyz')

# # strings are sequences
# # sequence — a positionally ordered collection of other objects.
# Sequences maintain a left-to-right order among the items they contain:
# their items are stored and fetched by their relative positions. Strictly speaking, strings
# are sequences of one-character strings; other, more general sequence types include
# lists and tuples, covered later.

s = 'hello'

print(len(s))  # built in len function allows to calculate the length of string: number of chars
print(len(s) == 5)

# In Python, indexes are coded as offsets from the front, and so start from 0: the first item
# is at index 0, the second is at index 1, and so on.

print(s[0])
print(s[1])
print(s[3])

# In Python, we can also index backward, from the end—positive indexes count from
# the left, and negative indexes count back from the right:

print(s[-1])  # the last item
print(s[-2])  # the item before the lsat item

# In addition to simple positional indexing, sequences also support a more general form
# of indexing known as slicing, which is a way to extract an entire section (slice) in a single
# step. For example:

# [Start index (included): Stop index (excluded)]
a = s[1:3]  # from item with index number 1 (including it) till item with number 3 (not including)
print(a)

a = s[:3]  # the same as s[0:3]
print(a)

a = s[2:]  # the same as s[2:len(s)]
print(a)

a = s[:-2]  # everything without last item
print(a)

s = '123456789'

# [start: end: step]

a = s[1::2]  # selecting each first then third and so one
print(a)

a = s[::-1]  # reversing
print(a)


# Also notice in the prior examples that we were not changing the original string with
# any of the operations we ran on it. Every string operation is defined to produce a new
# string as its result, because strings are immutable in Python—they cannot be changed
# in place after they are created.

# s[0] = 'j'

s = 'j' + s[1:]
print(s)

# String Formatting Operator
x = 'razmik'
y = 'adsygdkasd'
print('my name is {}'.format(x))
print(f'my name is {x + x} {x} + {y}')

x = 10.35253232323
a = 'number is approximately equal to {:.3f}'.format(x)
print('number is approximately equal to {:.3f}'.format(x))

default_order = "{}, {} and {}".format('John', 'Bill', 'Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John', 'Bill', 'Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John', b='Bill', s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)


# left alignment for word 'Cake' according to right alignment, gaps filled with '#'
print('{:?<10}'.format('Cake'))

# centre alignment for word 'Cake' according to right alignment, gaps filled with '#'
print('{:#^10}'.format('Cake'))



# Escape Sequence	Description
# \\	    Backslash
# \'	    Single quote
# \"	    Double quote
# \a        ASCII Bell
# \b	    ASCII Backspace
# \f	    ASCII Formfeed
# \n	    ASCII Linefeed
# \r	    ASCII Carriage Return
# \t	    ASCII Horizontal Tab
# \v	    ASCII Vertical Tab
# \ooo	    Character with octal value ooo
# \xHH	    Character with hexadecimal value HH

print('h\'ello')
print('h\aello')
print('h\bello')
print('h\tello')

# TODO: try all possible versions


# string built in methods

# Method	    Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	    Returns a centered string
# count()	    Returns the number of times a specified value occurs in a string
# encode()	    Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	    Searches the string for a specified value and returns the position of where it was found
# format()	    Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	    Searches the string for a specified value and returns the position of where it was found
# isalnum()	    Returns True if all characters in the string are alphanumeric
# isalpha()	    Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	    Returns True if all characters in the string are digits
# isidentifier()Returns True if the string is an identifier
# islower()	    Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	    Returns True if all characters in the string are whitespaces
# istitle()	    Returns True if the string follows the rules of a title
# isupper()	    Returns True if all characters in the string are upper case
# join()	    Joins the elements of an iterable to the end of the string
# ljust()	    Returns a left justified version of the string
# lower()	    Converts a string into lower case
# lstrip()	    Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	    Returns a string where a specified value is replaced with a specified value
# rfind()	    Searches the string for a specified value and returns the last position of where it was found
# rindex()	    Searches the string for a specified value and returns the last position of where it was found
# rjust()	    Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	    Splits the string at the specified separator, and returns a list
# rstrip()	    Returns a right trim version of the string'一二三四五'.isnumeric()
# split()	    Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	    Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	    Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	    Converts a string into upper case
# zfill()	    Fills the string with a specified number of 0 values at the beginning


a = 'raaaazmik'
print('my string is: {}'.format(a))
print(a.capitalize())
print(a.count('a'))
print(a.endswith('k'))
print(a.endswith('l'))
print('melikbekyan'.endswith('yan'))
print(a.find('zm'))
print(a.isalnum())
print('dsahdak!!!'.isalnum())
print(a.isalpha())
print('dsajld123'.isalpha())
print('dsajld123'.isalnum())
print('123'.isdigit())
print('asas33'.isdigit())
print('123,45'.isdigit())   # returns True for strings containing solely the digits 0-9
print('123.45'.isnumeric()) #  digits 0-9, plus any character from another language that’s used
                            # in place of digits
print('一二三四五'.isdigit())
print('一二三四五'.isnumeric())
print('\n'.join(['razmik', 'melikbekyan', 'sadkad', 'asdasd']))
print(a.replace('a', 'R'))
print(a)
print('Razmik Melikbekyan'.split())
print('Razmik Melikbekyan'.split('k'))
print('  Razmik Melikbekyan '.strip())



# TODO continue yourself with other methods



# Function	Description
# chr()	    Converts an integer to a character
# ord()	    Converts a character to an integer
# str()	    Returns a string representation of an object

print(chr(97))
print(chr(123))

print(ord('b'))
print(ord('?'))
print(ord('∑'))

print(str(122))
print(str(90.3331))
print(str(4 + 5j))


# Python allows for command line input.
# That means we are able to ask the user for input.
# The following example asks for the user's name, then, by using the input()
# method, the program prints the name to the screen:
print("Enter your name:")
x = input()
print(type(x))
print("Hello, {}".format(x))

