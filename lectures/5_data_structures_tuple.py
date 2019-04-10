# Tuples


# Python provides another type that is an ordered collection of objects, called a tuple.

# Tuples are identical to lists in all respects, except for the following properties:
#
# - Tuples are defined by enclosing the elements in parentheses
#   (()) instead of square brackets ([]).
# - Tuples are immutable.

from decimal import Decimal


def plus(x, y):
    return x + y


t = (1, 2, 3)
print(t)

t = ('a', int, plus, Decimal('5'), float, 12, 35.5, 6 + 4j)
print(t)

print(t[0])
print(t[-1])
print(t[2:4])
print(t[::-1])

# # immutable
# t[0] = 'aaaaaaa'
# print(t)


# Why use a tuple instead of a list?
#
#  - Program execution is faster when manipulating a tuple than it is for the equivalent list.
#   (This is probably not going to be noticeable when the list or tuple is small.)
#
#  - Sometimes you don’t want data to be modified. If the values in the collection are meant to
#    remain constant for the life of the program, using a tuple instead of a list guards
#    against accidental modification.
#
# - There is another Python data type that you will encounter shortly called a dictionary,
#   which requires as one of its components a value that is of an immutable type.
#   A tuple can be used for this purpose, whereas a list can’t be.

t = ()
print(type(t))

t = (1)
print(type(t))

t = (1,)
print(type(t))

# unpacking
t = (1, 2, 3)
a, b, c = t
print(a)
print(b)
print(c)

# a, b, c, d = t
# print(a)

# Packing and unpacking can be combined into one statement to make a compound assignment:
(a, b, c, d) = ('a', 'b', 'c', 'd')
print(a)

t = 1,
print(t)
print(type(t))

# Tuple assignment allows for a curious bit of idiomatic Python. Frequently when programming, you
# have two variables whose values you need to swap. In most programming languages, it is necessary
# to store one of the values in a temporary variable while the swap occurs like this:

a = 1
b = 2
print(f'a={a}, b={b}')

# We need to define a temp variable to accomplish the swap in most of programming languages.
temp = a
a = b
b = temp
print(f'a={a}, b={b}')

a = 1
b = 2
print(f'a={a}, b={b}')

# Magic time!
a, b = b, a
print(f'a={a}, b={b}')

# Tuple built in methods

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# TODO try them
# TODO try also in, not in, len, min, max, del, iteration, bool
