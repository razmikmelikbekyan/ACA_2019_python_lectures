# There are quite a few data structures available. The builtins data structures are:
# lists, tuples, dictionaries, sets.

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Lists, strings and tuples are ordered sequences of objects. Unlike strings that contain only
# characters, list and tuples can contain any type of objects. Lists and tuples are like arrays.
# Tuples like strings are immutables. Lists are mutables so they can be extended or reduced at
# will. Sets are mutable unordered sequence of unique elements.


# Lists

# In short, a list is a collection of arbitrary objects, somewhat akin to an array in many other
# programming languages but more flexible. Lists are defined in Python by enclosing a
# # comma-separated sequence of objects in square brackets ([]), as shown below:


a = ['foo', 'bar', 'baz', 'qux']
print(a)

# The important characteristics of Python lists are as follows:
#
# - Lists are ordered.
# - Lists can contain any arbitrary objects.
# - List elements can be accessed by index.
# - Lists can be nested to arbitrary depth.
# - Lists are mutable.
# - Lists are dynamic.


# - Lists Are Ordered


a = [1, 2, 's', '4', 3.4]
b = [1, 2, '4', 's', 3.4]
print(a == b)

a = [1, 2, 's', '4', 3.4]
b = [1, 2, 's', '4', 3.4]
print(a == b)
print(a is b)

# - Lists can contain any arbitrary objects

from decimal import Decimal

a = [1, 'int', 1.2, 'float', 1 + 2j, 'complex', True, 'boolean', Decimal('35'), 'decimal']
print(a)


def plus(x, y):
    return x + y


a = [plus, len, int]
print(a)

# A list can contain any number of objects, from zero to as many as your computer’s memory will
# allow.

# List objects needn’t be unique. A given object can appear in a list multiple times:
a = [1, 1, 's', 's']
print(a)

# - List Elements Can Be Accessed by Index - the rules are the same as for strings

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# indexes
print(a[0])  # the first element
print(a[1])  # the second
print(a[-1])  # the last one
print(a[-2])  # the item before the last one

# slicing
print(a[1:4])  # the items from index 1 (included) to index 4 (not included)
print(a[-4: -1])  # the items from index -4 (included) to index -1 (not included)
print(a[-4: -1] == a[len(a) - 4: len(a) - 1])

# striding
print(a[1:6:2])
print(a[::2])
print(a[::3])
print(a[5:0:-2])
print(a[::-1])

# copy: a[:] returns a new object that is a copy of a
b = a[:]
print(a is b)

# - in and not in operators

a = [1, 2, 's', Decimal('3')]

print(1 in a)
print(3 in a)
print(Decimal('3') in a)
print(int in a)
print(float not in a)
for x in a:
    print(x)
    if isinstance(x, int):
        print('int')

# concatenation (+) and replication (*) operators

a = [1, 2, 3, 3.4, Decimal('5.6')]
b = ['ac', 'ab', 'c', ]
c = a + b
print(c)

c = a * 3
print(c)

# len(), min(), and max() functions
print(len(a))
print(min(a))
print(max(a))

print(len(b))
print(min(b))
print(max(b))

# - Lists Can Be Nested
a = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(a)
print(len(a))

print(a[0])
print(len(a[1]))

print(a[1])
print(a[1][1])
print(a[1][1][1])

print(a[3])
print(a[3][0])

# - Lists Are Mutable

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)

a[0] = -25  # modifying the first element
print(a)

a[-1] = 56  # modifying the first element
print(a)

# The number of elements inserted need not be equal to the number replaced.
# Python just grows or shrinks the list as needed.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a[1:3] = [1.1, 2.5]
print(a)

a[1:3] = ['a', 'a', 'a'] * 3
print(a)

# You can insert multiple elements in place of a single element—just use a slice that
# denotes only one element:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[:] = ['j', 'k'] * (len(a) // 2)
print(a)

a[1:2] = ['b'] * 4
print(a)

# Note that this is not the same as replacing the single element with a list:
a[1] = ['b'] * 4
print(a)

# You can also insert elements into a list without removing anything. Simply specify a slice of
# the form [n:n] (a zero-length slice) at the desired index:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a[3:3] = [3 + 4j] * 2
print(a)

a.insert(3, [3 + 4j] * 2)
a.insert(3, 3 + 4j)
print(a)

# You can delete multiple elements out of the middle of a list by assigning the appropriate slice
# to an empty list. You can also use the del statement with the same slice:

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[1:4] = []

# Or you can use built in del function

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

del a[0]
print(a)

del a[1:3]
print(a)

# - Lists Are Dynamic

# When items are added to a list, it grows as needed:

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2:2] = [1, 2, 3]
print(a)

a += [3.14159]
print(a)

# List built in methods


# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

a = [1, 2, 3]

print(a)

a.append(4)
print(a)

a.clear()
print(a)

a = [1, 2, 3]
b = a.copy()  # a[:]
print(b)
print(a[0] is b[0])
print(a == b)

print(a.count(1))

a = ['s', 's', 's', int, int]
print(a)
print('count of "{}" in list a equal to "{}".'.format('s', a.count('s')))
print('count of "{}" in list a equal to "{}".'.format(int, a.count(int)))

a = [1, 2, 3]
b = ['a', 'b', 'c']
a.append(b)
print('result of "append" is {}'.format(a))

a = [1, 2, 3]
b = ['a', 'b', 'c']
a.extend(b)
print('result of "extend" is {}'.format(a))

print(a)
print(a.index(1))
print(a.index('b'))

a.append(1)
print(a)
print(a.index(1))
print(a.index(1, 1))

x = 'jj'
try:
    print(a.index(x))
except ValueError:
    print(f'{x} not in list')

# a small program, which returns all indexes of 1 in given list
a = ['a', 1, 2, 3, 1, 4, 1, 5]
count = a.count(1)
indexes = []
for i in range(count):
    print(f'step={i}')
    if i == 0:
        index = a.index(1)
    else:
        last_found_index = indexes[-1]
        index = a.index(1, last_found_index + 1)
    print(f'found index={index}')
    indexes.append(index)
    print(f'current indexes={indexes}')
    print()
print(indexes)

a = [1, 2, 3]
a.insert(0, 'inserted')
print(a)

a.insert(len(a), 'inserted')
print(a)

a.pop()  # if the position is not specified, will remove the last element
print(a)

b = a.pop(0)
print(a)
print(b)
print(a)

a.remove(1)  # removes the first occurrence of an object
print(a)

b = a.reverse()  # reversing
print(a)
a = [1, 3, 2]
print(a)

a.sort()
print(a)

a = [['a', 2, 3], ['c', 0, 5], ['b', 1, 2]]
print(a)
a.sort()
print(a)

a.sort(key=lambda x: x[1])
print(a)

# iteration
for element in a:
    print(element)

# an empty list in python is False
a = []
print(bool(a))
