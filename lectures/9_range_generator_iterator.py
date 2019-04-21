# ******************************************range class*******************************************

#  The range() class return an object that produces a sequence of integers from start (inclusive)
#  to stop (exclusive) by step.
#  range(i, j) produces i, i+1, i+2, ..., j-1.
#  Start defaults to 0, and stop is omitted!
#  range(4) produces 0, 1, 2, 3.
#  These are exactly the valid indices for a list of 4 elements.
#  When step is given, it specifies the increment (or decrement).

# Syntax

# range(start, stop, step)

# start -> Optional. An integer number specifying at which position to start. Default is 0
# stop -> Optional. An integer number specifying at which position to end.
# step -> Optional. An integer number specifying the incrementation. Default is 1

# The end value is excluded from the sequence.

# Example 1:

# Create a sequence of numbers from 3 to 5, and print each item in the sequence:
for num in range(3, 6):
    print(num)

# Example 2:

# Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
for num in range(3, 20, 2):
    print(num)

# Example 3:

# Decrementing with help of range:

for num in range(10, -6, -2):
    print(num)

# ********************************************Iterators********************************************

# We use for statement for looping over a list.
for i in [1, 2, 3, 4]:
    print(i)

# If we use it with a string, it loops over its characters.
for c in "python":
    print(c)

# If we use it with a dictionary, it loops over its keys.
for k in {'x': 1, 'y': 2}.keys():
    print(k)

# If we use it with a file, it loops over lines of the file.


# So there are many types of objects which can be used with a for loop.
# These are called iterable objects. There are many functions which consume these iterables.

print(','.join(['a', 'b', 'c']))
print(','.join({'x': 1, 'y': 2}))
print(list('Iteration'))
print(list({'x': 1, 'y': 2}))

# Term	        Meaning
# Iteration	    The process of looping through the objects or items in a collection
# Iterable	    An object (or the adjective used to describe an object) that can be iterated over
# Iterator	    The object that produces successive items or values from its associated iterable
# iter()	    The built-in function used to obtain an iterator from an iterable


# The Iteration Protocol

# The built-in function iter takes an iterable object and returns an iterator object.

iterator_object = iter(["a", "b", "c"])
print(type(iterator_object))

iterator_object = iter((1, 2, 3))
print(type(iterator_object))

iterator_object = iter({1, 2, 3})
print(type(iterator_object))

iterator_object = iter("sjadjad")
print(type(iterator_object))

iterator_object = iter({'a': 1, 'b': 2})
print(type(iterator_object))

# An iterator is essentially a value producer that yields successive values from its associated
# iterable object. The built-in function next() is used to obtain the next value from in iterator.

iterator_object = iter(["a", "b", "c"])
print(type(iterator_object))

# 1
print(next(iterator_object))

# 2
print(next(iterator_object))

# 3
print(next(iterator_object))

# Each time we call the next function on the iterator gives us the next element. If there are no
# more elements (iterator is exhausted), it raises a StopIteration error.
try:
    print(next(iterator_object))
except StopIteration:
    print('iterator is exhausted')

# in order to not raising this error, you can use default value argument for the next function
# (like for the get of dict) and it will return this default value instead of raising en exception
print(next(iterator_object, "iterator is exhausted"))


# ***************************************Generators************************************************

# Generator functions allow you to declare a function that behaves like an iterator, i.e.
# it can be used in a for loop. They can be paused and resumed on the fly, returning an object
# that can be iterated over. Unlike lists, they are lazy and thus produce items one at a time and
# only when asked. So they are much more memory efficient when dealing with large datasets.

# To create a generator, you define a function as you normally would but use the yield statement
# instead of return, indicating to the interpreter that this function should be treated as an
# iterator:

def y_range(n):
    print("start from {n}")
    i = 0
    while i < n:
        yield i
        i += 1


# The yield statement pauses the function and saves the local state so that it can be resumed right
# where it left off.

# What happens when you call this function?
y_generator = y_range(3)
print(f"y type is {type(y_generator)}")

# Calling the function does not execute it. We know this because the string "Start from {n}" did not
# print. Instead, the function returns a generator object which is used to control execution.

# Generator objects execute when next() is called:
print(next(y_generator))

# When calling next() the first time, execution begins at the start of the function body and
# continues until the next yield statement where the value to the right of the statement is
# returned, subsequent calls to next() continue from the yield statement to the end of the
# function, and loop around and continue from the start of the function body until another yield
# is called. If yield is not called (which in our case means we don’t go into the if function
# because i >= n) a StopIteration exception is raised:

print(next(y_generator))
print(next(y_generator))
print(next(y_generator))


# for loop
for x in y_generator:
    print(x)

# Alternatively you can call a next function and pass generator object.
print(next(y_generator, 'generator is exhausted'))


# Each time the yield statement is executed the function generates a new value.


# When a generator function is called, it returns a generator object without even beginning
# execution of the function. When next method is called for the first time, the function starts
# executing until it reaches yield statement. The yielded value is returned by the next call.

# The following example demonstrates the interplay between yield
# and call to next method on generator object.

def foo():
    print('begin')
    for num in range(3):
        print(f'before yield num={num}')
        yield num
        print(f'after yield num={num}')
    print('end')


f = foo()
print(next(f))
print(next(f))
print(next(f))
print(next(f, "generator is exhausted"))


# after yield 2
# end
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>>

# After yielding all the values next() caused a StopIteration error.
# What this error informs us of is that all the values have been yielded.

# Fibonacci problem

def fibonacci(number):
    x, y = 0, 1
    while x < number:
        yield x
        x, y = y, x + y


fibonacci_generator = fibonacci(1000000)
for fibonacci_number in fibonacci_generator:
    print(fibonacci_number)

# Note that once we have “consumed” the generator, we can’t use it anymore because generators
# in Python can’t be rewound. So, if after the code above we tried to print out all the sequence
# again, we won’t get any values.
for x in fibonacci_generator:
    print('aaaaaaaaaaaaaaaaaaaaaaaaa')

# Generator expressions


# Generator Expressions are generator version of list comprehensions.
# They look like list comprehensions, but returns a generator back instead of a list.

a = (x * x for x in range(10))
print(f"a type is {type(a)}")

# Generator expressions can be used as arguments for various functions that accepts iterators.
print(sum(a))
print(max(x * x for x in range(10)))
