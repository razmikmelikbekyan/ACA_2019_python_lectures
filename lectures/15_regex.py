# *******************************************RegEx*************************************************

# In this lecture we will learn how to use Regular Expression for search. Regular expressions,
# also called regex is implemented in pretty much every computer language. In python, it is
# implemented in the standard module re.

import re

# It is widely used in natural language processing, web applications that require validating string
# input (like email address) and pretty much most data science projects that involve text mining.


# ************************************Part 1: RegEx Pattern****************************************

# A regex pattern is a special language used to represent generic text, numbers or symbols so it
# can be used to extract texts that conform to that pattern


# A basic example is: '\s+'

# Here the '\s' matches any whitespace character. By adding a '+' notation at the end will make the
# pattern match at least 1 or more spaces. So, this pattern will match even tab '\t' characters as
# well.

pattern = re.compile('\s+')

text = """101 COM    Computers
205 MAT   Mathematics
189 ENG   English"""

# The spacing between the words are not equal.

# I want to split these three course items into individual units of numbers and words.
# How to do that?


# Solution 1: using python str class split() method - string.split()
print(text.split())

# Solution 2: using RegEx pattern split() method - pattern.split(text)
print(pattern.split(text))

# Let’s suppose you want to extract all the course numbers, that is, the numbers 101, 205 and 189
# alone from the above text. How to do that?

# We can do it with pattern.findall(text) method.
pattern = re.compile('\d+')
print(pattern.findall(text))

# In above code, the special character '\d' is a regular expression which matches any digit.

# Similar to '+', there is a '*' symbol which requires 0 or more digits in order to be found.
# It practically makes the presence of a digit optional in order to make a match.

# Finally, the findall method extracts all occurrences of the 1 or more digits from the text and
# returns them in a list.


# If we want to find the positions of searching text, we can use pattern.search() method.
text = """COM    Computers
205 MAT   Mathematics 189"""

pattern = re.compile('\d+')
search_obj = pattern.search(text)

# it returns match object that contains the starting and ending positions of the first occurrence
# of the pattern.
print(type(search_obj))

print('Starting Position: ', search_obj.start())
print('Ending Position: ', search_obj.end())
print(text[search_obj.start():search_obj.end()])

# Alternately, you can get the same output using the group() method of the match object.
print(search_obj.group())

# Likewise, pattern.match() also returns a match object. But the difference is, it requires the
# pattern to be present at the beginning of the text itself.
print(pattern.match(text))
print(pattern.match("152 asda 1454"))
print(pattern.match("152 asda 1454").group())

# If we want to replace one string with another one, we can use pattern.sub(new_string, text).

text = """101 COM    Computers
205 MAT   Mathematics
189 ENG   English"""

# Lets replace multiple whitespace with just one.
pattern = re.compile('\s+')
print(pattern.sub(' ', text))

# or
print(re.sub('\s+', ' ', text))

# Please note that it removes not only spaces but also new lines and tabs. Generally in python
# whitespaces are the following items:
import string

print(f'white spaces are: {list(string.whitespace)}')

# Suppose you only want to get rid of the extra spaces but want to keep the course entries in the
# new line itself. To achieve that you should use a regex that effectively excludes new line
# characters but includes all other whitespaces.

# This can be done using a negative lookahead (?!\n). It checks for an upcoming newline character
# and excludes it from the pattern.

print(re.sub('((?!\n)\s+)', ' ', text))

# Or you can use RegEx pattern ' +' for 1 or more spaces:
print(re.sub(' +', ' ', text))

# ************************************Part 2: RegEx groups*****************************************


# Regular expression groups is a very useful feature that lets you extract the desired match
# objects as individual items.


# Suppose I want to extract the course number, code and the name as separate items. Without groups,
# I will have to write something like this.

text = """101   COM   Computers
205   MAT   Mathematics
189   ENG    English"""

# 1. extract all course numbers
number = re.findall('[0-9]+', text)
print(number)

# The pattern [0-9]+ instructs to match all number from 0 to 9. Adding a + symbol at the end makes
# it look for at least 1 occurrence of numbers 0-9. If you know the course number will certainly
# have exactly 3 digits, the pattern could have been [0-9]{3} instead.


# 2. extract all course codes
code = re.findall('[A-Z]{3}', text)
print(code)

# The pattern '[A-Z]{3}' will match exactly 3 consecutive occurrences of alphabets capital A-Z.


# 3. extract all course names
name = re.findall('[A-Za-z]{4,}', text)
print(name)

# The pattern '[A-Za-z]{4,}' will look for upper and lower case alphabets a-z, assuming all course
# names will have at least 4 or more characters.


# Now I had to write 3 separate lines to get the individual items.
# But there is a better way - RegEx Groups.

# Since all the entries have the same pattern, you can construct a unified pattern for the entire
# course entry and put the portions you want to extract inside a pair of brackets ().

course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
print(re.findall(course_pattern, text))

# Greedy matching

# The default behavior of regular expressions is to be greedy. That means it tries to extract as
# much as possible until it conforms to a pattern even when a smaller part would have been
# syntactically sufficient.

text = "< body>Regex Greedy Matching Example < /body aaa>"
print(re.findall('<.*>', text))

# Instead of matching till the first occurrence of ‘>’, which I was hoping would happen at the end
# of first body tag itself, it extracted the whole string. This is the default greedy or
# ‘take it all’ behavior of regex.

# Lazy matching, on the other hand, ‘takes as little as possible’. This can be effected by adding
# a `?` at the end of the pattern.

print(re.findall('<.*?>', text))

# If you want only the first match to be retrieved, use the search method instead.
print(re.search('<.*?>', text).group())

# *******************************Part 3: Common RegEx syntax***************************************

# BASIC SYNTAX

# .             One character except new line
# \.            A period. \ escapes a special character.
# \d            One digit
# \D            One non-digit
# \w            One word character including digits
# \W            One non-word character
# \s            One whitespace
# \S            One non-whitespace
# \b            Word boundary
# \n            Newline
# \t            Tab


# MODIFIERS

# $             End of string
# ^             Start of string
# ab|cd         Matches ab or de.
# [ab-d]	    One character of: a, b, c, d
# [^ab-d]	    One character except: a, b, c, d
# ()            Items within parenthesis are retrieved
# (a(bc))       Items within the sub-parenthesis are retrieved


# REPETITIONS

# [ab]{2}       Exactly 2 continuous occurrences of a or b
# [ab]{2,5}     2 to 5 continuous occurrences of a or b
# [ab]{2,}      2 or more continuous occurrences of a or b
# +             One or more
# *             Zero or more
# ?             0 or 1


# ***********************************Part 4: Examples**********************************************

text = 'hello \n 2555 52 world.com'

# Any character except for a new line:
print(re.findall('.', text))  # .   Any character except for a new line
print(re.findall('...', text))

# A period:
print(re.findall('\.', text))  # matches a period
print(re.findall('[^\.]', text))  # matches anything but a period

# Any digit:
print(re.findall('\d+', text))  # \d  Any digit. The + mandates at least 1 digit.

# Anything but a digit:
print(re.findall('\D+', text))  # \D  Anything but a digit

# Any character, including digits:
print(re.findall('\w+', text))  # \w  One word character including digits

# Anything but a character:
print(re.findall('\W+', text))  # \W  Anything but a character

# Collection of characters:
print(re.findall('[a-zA-Z]+', text))  # [] Matches any character inside

# Match something upto ‘n’ times:
print(re.findall('\d{4}', text))  # {n} Matches repeat n times.
print(re.findall('\d{2,4}', text))
