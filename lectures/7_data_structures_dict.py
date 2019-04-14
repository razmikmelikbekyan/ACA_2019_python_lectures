# Python provides another composite data type called a dictionary, which is similar to a list in
# that it is a collection of objects.
#
# Dictionaries and lists share the following characteristics:
#
# - Both are mutable.
# - Both are dynamic. They can grow and shrink as needed.
# - Both can be nested. A list can contain another list. A dictionary can contain another
#   dictionary.
# - A dictionary can also contain a list, and vice versa.
#
# Dictionaries differ from lists primarily in how elements are accessed:
#
# - List elements are accessed by their position in the list, via indexing.
# - Dictionary elements are accessed via keys.


# Defining a Dictionary

# A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its
# associated value.
#
# You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly
# braces ({}). A colon (:) separates each key from its associated value:
#
# d = {
#     <key>: <value>,
#     <key>: <value>,
#       .
#       .
#       .
#     <key>: <value>
# }

# lets define {city: football_team} pairs
teams = {
    'Milan': 'Milan',
    'Turin': 'Juventus',
    'Jenova': 'Sampdoria',
    'Bergamo': 'Atalanta',
    'Florence': 'Fiorentina',
    'Rome': 'Lazio',
    'Udine': 'Udinese'
}
print(teams)
print(type(teams))

# please note that we defined dict using the same "{" as for sets, but there is a simple rule in
# python: if there are {key: value} pairs inside "{}", then it is a dictionary, if there are only
# values: {value_1, value_2, ...} then it is a set.

# We can define dicts also using constructor "dict"

# from list of tuples
teams = dict([
    ('Milan', 'Milan'),
    ('Turin', 'Juventus'),
    ('Jenova', 'Sampdoria'),
    ('Bergamo', 'Atalanta'),
    ('Florence', 'Fiorentina'),
    ('Rome', 'Lazio'),
    ('Udine', 'Udinese')
])
print(teams)
print(type(teams))

# If the key values are simple strings, they can be specified as keyword arguments.
# So here is yet another way to define MLB_team:
teams = dict(
    Milan='Milan',
    Turin='Juventus',
    Jenova='Sampdoria',
    Bergamo='Atalanta',
    Florence='Fiorentina',
    Rome='Lazio',
    Udine='Udinese'
)
print(teams)
print(type(teams))

# Dictionaries do not have indexes, so it is not possible to get entries using indexes
try:
    print(teams[1])
except KeyError:
    print('dictionary is not indexed')

# Accessing Dictionary Values

# A value is retrieved from a dictionary by specifying its corresponding key in square brackets
# ([]):

print(teams['Turin'])
print(teams['Rome'])

# If you refer to a key that is not in the dictionary, Python raises an exception (KeyError):
try:
    print(teams['Parma'])
except KeyError:
    print('Parma is not in dictionary.')

# Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:
teams['Parma'] = 'Parma'
print(teams)

# To delete an entry, use the del statement, specifying the key to delete:
del teams['Parma']
print(teams)

# Restrictions on Dictionary Keys

# There are 2 restrictions on dictionary keys:

# - a dictionary key must be of a type that is immutable (int, str, float, tuple, boolean, ...)
#   (More precisely, an object must be hashable, which means it can be passed to a hash function.
#   A hash function takes data of arbitrary size and maps it to a relatively simpler fixed-size
#   value called a hash value (or simply hash), which is used for table lookup and comparison.)
# - a given key can appear in a dictionary only once. Duplicate keys are not allowed. A dictionary
#   maps each key to a corresponding value, so it does n’t make sense to map a particular key more
#   than once.

foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
print(foo)

foo = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
print(foo)

try:
    foo = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
    print(foo)
except TypeError:
    print('dictionary keys must be hashable')

# Restrictions on Dictionary Values

# - By contrast, there are no restrictions on dictionary values. Literally none at all.
#   A dictionary value can be any type of object Python supports, including mutable types like
#   lists and dictionaries, and user-defined objects.


foo = {'a': [1, 2, 3], 1: (2, 3), 4: {1, 3, 1}, 'b': 4 + 6j}
print(foo)

# Restrictions on Dictionary Values


# Building a Dictionary Incrementally

foo = {}
print(foo)
print(type(foo))

# You can start by creating an empty dictionary, which is specified by empty curly braces.
# Then you can add new keys and values one at a time:
foo['name'] = 'Razmik'
foo['title'] = 'Mr'

for i in range(5):
    foo[i] = i ** 2

foo['a'] = 'hello'
print(foo)

# Note: Although access to items in a dictionary does not depend on order, Python does guarantee
# that the order of items in a dictionary is preserved. When displayed, items will appear in the
# order they were defined, and iteration through the keys will occur in that order as well.
# Items added to a dictionary are added at the end. If items are deleted, the order of the
# remaining items is retained.
#
# You can only count on this preservation of order very recently. It was added as a part of the
# Python language specification in version 3.7. However, it was true as of version 3.6 as well—by
# happenstance as a result of the implementation but not guaranteed by the language specification.

# Operators and Built-in Functions

foo = {'a': [1, 2, 3], 1: (2, 3), 4: {1, 3, 1}, 'b': 4 + 6j}

# in and not in allows to check if the specific key is in dict or not
print('a' in foo)
print('c' in foo)
print('c' not in foo)

# len - the number of key-value pairs
print(len(foo))

# max, min - the maximum and minimum of keys
foo = {1: 1, 2: 4, 3: 9, 4: 16}
print(max(foo))
print(min(foo))

# empty dict is False
foo = {}
print(bool(foo))
if foo:
    print('dictionary is not empty')

foo = {1: 2}
print(bool(foo))

# Dictionary built in methods

# Method	    Description
# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and values
# get()	        Returns the value of the specified key
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist:
#                       insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# items()	    Returns a list containing the a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# values()	    Returns a list of all the values in the dictionary

# clear
foo = {}
for i in range(1, 6):
    foo[i] = i ** 2
print(foo)

foo.clear()
print(foo)

# copy
foo = {}
for i in range(1, 6):
    foo[i] = i ** 2
print(foo)

foo_2 = foo.copy()
print(foo_2)

# please not that if you have complex objects as values, then you need to do deepcopy
from copy import deepcopy

foo = {}
for i in range(1, 6):
    foo[i] = [i ** 2, i ** 3]
print(foo)

foo_copy = foo.copy()
foo_deepcopy = deepcopy(foo)

# not lets change value in foo and check what is happening with foo_copy and foo_deepcopy
foo[1].append('aaaaaaaaaaa')

print(f'foo = {foo}')
print(f'foo_copy = {foo_copy}')
print(f'foo_deepcopy = {foo_deepcopy}')

print(foo[1] is foo_copy[1])
print(foo[1] is foo_deepcopy[1])

# fromkeys
x = ('key1', 'key2', 'key3')
y = 0
foo = dict.fromkeys(x, y)
print(foo)

# get
# The .get() method provides a convenient way of getting the value of a key from a dictionary
# without checking ahead of time whether the key exists, and without raising an error.
#
# d.get(<key>) searches dictionary d for <key> and returns the associated value if it is found.
# If <key> is not found, it returns None:
foo = {}
for i in range(1, 6):
    foo[i] = [i ** 2, i ** 3]
print(foo)

print(foo.get(1))
print(foo.get(2))

# if key is not in dict, get returns default value (which is None)
print(foo.get('a'))
print(foo.get('a', 78))

# pop
# If <key> is present in d, d.pop(<key>) removes <key> and returns its associated value:
foo = {}
for i in range(1, 6):
    foo[i] = [i ** 2, i ** 3]
print(foo)

value = foo.pop(1)
print(value)
print(foo)

# d.pop(<key>) raises a KeyError exception if <key> is not in d:
try:
    value = foo.pop('a')
    print(value)
    print(foo)
except KeyError:
    print('a not in foo')

# If <key> is not in d, and the optional <default> argument is specified, then that value is
# returned, and no exception is raised:
value = foo.pop('a', 6787)
print(value)
print(foo)

# popitem
# d.popitem() removes a random, arbitrary key-value pair from d and returns it as a tuple:
foo = {}
for i in range(1, 6):
    foo[i] = [i ** 2, i ** 3]
print(foo)

item = foo.popitem()
print(item)

item = foo.popitem()
print(item)

# If d is empty, d.popitem() raises a KeyError exception:
foo.clear()
try:
    item = foo.popitem()
    print(item)
except KeyError:
    print('foo is empty')

# update(<obj>)
# Merges a dictionary with another dictionary or with an iterable of key-value pairs.

# If the key is not present in d, the key-value pair from <obj> is added to d.
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'e': 200, 'd': 400}

d1.update(d2)
print(d1)

# If the key is already present in d, the corresponding value in d for that key is updated to the
# value from <obj>.
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d1.update(d2)
print(d1)

d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update([('b', 200), ('d', 400)])
print(d1)

# items(), key   s(), values()
# items - Returns a list of key-value pairs in a dictionary.
# keys - Returns a list of keys in a dictionary.
# values - Returns a list of values in a dictionary
foo = {'a': 10, 'b': 20, 'c': 30}

items = list(foo.items())
print(items)

keys = list(foo.keys())
print(keys)

values = list(foo.values())
print(values)

# Technical Note: The .items(), .keys(), and .values() methods actually return something called a
# view object. A dictionary view object is more or less like a window on the keys and values.
# For practical purposes, you can think of these methods as returning lists of the dictionary’s
# keys and values.

# iterating over dict using items, keys and values

for key, value in foo.items():
    print(f'key={key}, value={value}')

for key in foo.keys():
    print(key)

for value in foo.values():
    print(value)

# sorting dictionary
foo = {'a': 2, 'c': 3, 'b': 4, 'd': 1}

# sorting by keys
foo = dict(sorted(foo.items()))
print(foo)

# sorting by keys in reversed order
foo = dict(sorted(foo.items(), reverse=True))
print(foo)

# sorting by values
foo = dict(sorted(foo.items(), key=lambda x: x[1]))
print(foo)

# explanation: dict.items() is an iterable of tuple(key, value)
# lambda x: x[1] returns the value under tuple index 1, which is actually dict values

# sorting by values in reversed order
foo = dict(sorted(foo.items(), key=lambda x: x[1], reverse=True))
print(foo)
