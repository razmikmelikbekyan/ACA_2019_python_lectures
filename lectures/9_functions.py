# ********************************************Functions********************************************

# In simple terms, a function is a device that groups a set of statements so they can be run
# more than once in a program—a packaged procedure invoked by name. Functions also
# can compute a result value and let us specify parameters that serve as function inputs
# and may differ each time the code is run. Coding an operation as a function makes it
# a generally useful tool, which we can use in a variety of contexts.

# More fundamentally, functions are the alternative to programming by cutting and pasting—rather
# than having multiple redundant copies of an operation’s code, we can factor it into a single
# function. In so doing, we reduce our future work radically: if the operation must be changed
# later, we have only one copy to update in the function, not many scattered throughout the
# program.

# Example:

# Suppose that you need to find the sum of integers from 1 to 10 , 20 to 37 , and 35 to 49 . If you
# create a program to add these three sets of numbers, your code might look like this:

result = 0
for x in range(1, 11):
    result += x
print("Sum from 1 to 10 is {}".format(result))

result = 0
for x in range(20, 38):
    result += x
print("Sum from 20 to 37 is {}".format(result))

result = 0
for x in range(35, 50):
    result += x
print("Sum from 35 to 49 is {}".format(result))


# So instead of copy and past the same logic of code, we can define a function and call it for
# different start and end.
def sum_integers_within_range(i_1, i_2):
    result = 0
    for x in range(i_1, i_2):
        result += x
    print(f'Sum from {i_1} to {i_2} is equal to {result}')
    return result


sum_integers_within_range(1, 11)
sum_integers_within_range(20, 38)
sum_integers_within_range(35, 50)


# Functions are also the most basic program structure Python provides for maximizing code reuse,
# and lead us to the larger notions of program design. As we’ll see, functions let us split complex
# systems into manageable parts. By implementing each part as a function, we make it both reusable
# and easier to code.


# Functions serve two primary development roles:
# - Maximizing code reuse and minimizing redundancy
# - Procedural decomposition

# General syntax

# def function_name(arguments, key_word_arguments):
#     statement_1
#     statement_2
#     ***********
#     return some_value (optional)

# As with all compound Python statements, def consists of a header line followed by a
# block of statements, usually indented (or a simple statement after the colon). The
# statement block becomes the function’s body—that is, the code Python executes each
# time the function is later called.
#
# The def header line specifies a function name that is assigned the function object, along
# with a list of zero or more arguments (sometimes called parameters) in parentheses.
# The argument names in the header are assigned to the objects passed in parentheses at
# the point of call.

# Function bodies often contain a return statement.
# The Python return statement can show up anywhere in a function body; when reached,
# it ends the function call and sends a result back to the caller. The return statement
# consists of an optional object value expression that gives the function’s result. If the
# value is omitted, return sends back a None .

# Example:

# function with return statement
def multiply(x, y):
    return x * y


value = multiply(3.5, 6.7)
print(f'function result is "{value}"')


# Example:

# function without return statement
def f_message(message):
    print('hello')
    print(f'here is your message \n{message}')


value = f_message('I am a function without return statement')
print(f'function result is "{value}"')


# def Executes at Runtime
# The Python def is a true executable statement: when it runs, it creates a new function
# object and assigns it to a name. (Remember, all we have in Python is runtime (dynamic); there is
# no such thing as a separate compile time.) Because it’s a statement, a def can appear
# anywhere a statement can—even nested in other statements. For instance, although
# def s normally are run when the module enclosing them is imported, it’s also completely
# legal to nest a function def inside an if statement to select between alternative definitions:

# Example:

# redefining function
def f(x, y):
    print('I am a sum function')
    return x + y


print(f(4, 5))


def f(x, y):
    print('I am a multiply function')
    return x * y


print(f(4, 5))

# Example:

# We can define function even in if else:

output = 'sum'

if output == 'sum':
    def f(x, y):
        return x + y
else:
    def f(x, y):
        return x * y

print(f(10, 25))

# Example:

# We can assign a function to a variable:

new_name = f
print(type(new_name))
print(new_name)
print(new_name(10, 25))


# def is not evaluated until it is reached and run, and the code inside def is not evaluated until
# the functions are later called.

# A function’s arguments can be passed as positional arguments or keyword arguments.
# The power of a function is its ability to work with parameters. When calling a function, you
# need to pass arguments to parameters. There are two kinds of arguments: positional arguments
# and keyword arguments. Using positional arguments requires that the arguments be passed in
# the same order as their respective parameters in the function header.
# For example, the following function prints a message n times:

def n_print_message(message, n):
    for _ in range(n):
        print(message)


n_print_message('hello', 3)


# The statement above passes 'hello' -> message and 3 -> n. If we mix the positions of message
# and n, we will get an error:

# n_print_message(3, 'hello')

# When we call a function like this, it is said to use positional arguments. The arguments must
# match the parameters in order, number, and compatible type, as defined in the function header.


# You can also call a function using keyword arguments, passing each argument in the form
# name = value.

def n_print_message(message, n=3):
    for _ in range(n):
        print(message)


# In this case the default value of n is 3 and we can call function without specifying the
# value of n and it will use its default value:

n_print_message('hi')

# If we want to to call it with different n, we should specify new n with n=new_value:
n_print_message('hi', n=2)


# Please note, that the positional arguments cannot appear after any keyword arguments. So if we
# call the function like this: n_print_message(n=2, 'hi'), we will get an syntax error.

# n_print_message(n=2, 'hi')

# It is possible also to call positional arguments as keyword ones:
def f(x, y, z):
    return x * y * z


value = f(1, 2, 3)  # normal calling
print(value)

value = f(1, y=2, z=3)  # calling arg and as kwargs
print(value)

value = f(x=1, y=2, z=3)  # calling as kwargs
print(value)

value = f(y=2, x=1, z=3)  # calling as kwargs, with mixed orders
print(value)


# TODO move down
# As we just saw, the very meaning of the expression x * y in our simple times function
# depends completely upon the kinds of objects that x and y are—thus, the same function
# can perform multiplication in one instance and repetition in another. Python leaves it
# up to the objects to do something reasonable for the syntax. Really, * is just a dispatch
# mechanism that routes control to the objects being processed.
# This turns out to be a crucial philosophical difference between Python and statically
# typed languages like C++ and Java: in Python, your code is not supposed to care about
# specific data types.

# Generally speaking there are the following options:

def f(*name, garegin):
    print(name)
    print(garegin)
    return sum(name) * garegin


print(f(1, 1, 4, garegin=4))

#
# def f(*args):
#     return sum(args)
#
#
# print(f(1))
