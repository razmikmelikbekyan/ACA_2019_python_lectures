# Sets


# In mathematics, a rigorous definition of a set can be abstract and difficult to grasp.
# Practically though, a set can be thought of simply as a well-defined collection of distinct
# objects, typically called elements or members.
#
# Grouping objects into a set can be useful in programming as well, and Python provides a
# built-in set type to do so. Sets are distinguished from other object types by the unique
# operations that can be performed on them.

# Python’s built-in set type has the following characteristics:
#
#  - Sets are unordered.
#  - Set elements are unique. Duplicate elements are not allowed.
#  - A set itself may be modified, but the elements contained in the set must be of an
#    immutable type.


a = {1, 2, 1}
print(a)
print(type(a))

a = [1, 2, 1]
a = set(a)
print(a)

# Strings are also iterable, so a string can be passed to set() as well. You have already seen
# that list(s) generates a list of the characters in the string s.
# Similarly, set(s) generates a set of the characters in s:
string = 'razmik'
print(list(string))
print(set(string))

# An empty set is falsy in Boolean context:
a = set()
if a:
    print('a is not empty')

a = {1}
if a:
    print('a is not empty')

# the elements in a set can be objects of different types:
a = {42, 'foo', 3.14159, None}
print(a)

# Don’t forget that set elements must be immutable. For example, a tuple may be included in a set:
a = {42, 'foo', (1, 2, 3), 3.14159}
print(a)

# a = {42, 'foo', [1, 2, 3], 3.14159}
# print(a)


# Set Size and Membership
s = {1, 1, 1, 2, 2}
print(len(s))

print('a' in s)
print(1 in s)

# iteration
for x in s:
    print(x)

# Set built in methods
#
# Method	        Description
# add()	            Adds an element to the set
# clear()	        Removes all the elements from the set
# copy()	        Returns a copy of the set
# difference()	    Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	        Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	    Returns whether two sets have a intersection or not
# issubset()	    Returns whether another set contains this set or not
# issuperset()	    Returns whether this set contains another set or not
# pop()	            Removes an element from the set
# remove()	        Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	        Return a set containing the union of sets
# update()	        Update the set with the union of this set and others

a = {1, 2, 3, 1}
print(a)

a.add(1)
print(a)

a.add('aaa')
print(a)

b = {1, 2}
print(a.difference(b))  # elements which are in a and not in b
print(a - b)

a.discard(3)
print(a)

print(a.intersection(b))  # elements which are in both a and b
print(a & b)

c = {1}
print(a.intersection(b, c))  # elements which are in a and b and c

d = {'bbb'}
print(a)
print(a.isdisjoint(d))

# If x1.isdisjoint(x2) is True, then x1 & x2 is the empty set:
print(a & d)

print(a)
print(c)
print(c.issubset(a))  # checks if all elements of c is in a
print(c <= a)

print(a)
print(c)
print(a.issuperset(c))  # checks if a contains all elements of c
print(a >= c)

print(a)
print(d)
print(a.union(d))  # creates a new sets from elements of a and d
print(a | d)

e = {1, 'eeee'}
print(a)
print(e)
print(a.symmetric_difference(e))  # return the set of all elements in either a or e, but not both
print(a ^ e)

print(a)
print(e)
a.update(e)  # modify a set by union  # a = a | e or a |= e
print(a)

print(a)
l = a.pop()  # x.pop() removes and returns an arbitrarily chosen element from x.
print(l)
print(a)

# TODO try other methods
# TODO try also min, max, del, iteration, bool
