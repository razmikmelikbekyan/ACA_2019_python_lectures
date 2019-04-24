# ********************************************Functions********************************************


# **************************************Part 1: Basic syntax***************************************

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


def f(x, y):
    print('I am a multiply function')
    return x * y


print(f(['l'], 3))
print(f(('l'), 3))
print(f(4.5, 3))
print(f(3 + 5j, 6))
print(f(2, 2))

# As we just saw, the very meaning of the expression x * y in our simple f function depends
# completely upon the kinds of objects that x and y are—thus, the same function can perform
# multiplication in one instance and repetition in another. Python leaves it up to the objects to
# do something reasonable for the syntax. Really, * is just a dispatch  mechanism that routes
# control to the objects being processed.


# Moreover, if the objects passed in do not support this expected interface, Python will detect the
# error when the * expression is run and raise an exception automatically. It’s therefore usually
# pointless to code error checking ourselves. In fact, doing so would limit our function’s utility,
# as it would be restricted to work only on objects whose types we test for.

try:
    print(f(['aa'], 3.2))
except TypeError as e:
    print(e)

# This turns out to be a crucial philosophical difference between Python and statically typed
# languages like C++ and Java: in Python, your code is not supposed to care about specific data
# types. This sort of type-dependent behavior is known as polymorphism. In fact, every operation is
# a polymorphic operation in Python: printing, indexing, the * operator, and much more.


# ***************************************Part 2: Scopes********************************************

# In this part we will discuss variables defining and looking up. For this we introduce scopes —
# the places where variables are defined and looked up.

# Just about everything related to names, including scope classification, happens at assignment
# time in Python. As we’ve seen, names in Python spring into existence when they are first assigned
# values, and they must be assigned before they are used. Because names are not declared ahead of
# time, Python uses the location of the assignment of a name to associate it with a particular
# namespace. In other words, the place where you assign a name in your source code determines the
# scope it will live in, and hence its scope of visibility.

# Besides packaging code for reuse, functions add an extra namespace layer to your programs to
# minimize the potential for collisions among variables of the same name—by default, all names
# assigned inside a function are associated with that function’s namespace, and no other.

# This rule means that:

# • Names assigned inside a def can only be seen by the code within that def . You
#   cannot even refer to such names from outside the function.

# • Names assigned inside a def do not clash with variables outside the def , even if the
#   same names are used elsewhere. A name X assigned outside a given def (i.e., in a
#   different def or at the top level of a module file) is a completely different variable
#   from a name X assigned inside that def .


# Example

X = 5  # variable 1


def f(a):
    X = '***hello***'  # variable 2
    print(X)
    return a + X


print(X)
print(f('Jon'))

# In all cases, the scope of a variable (where it can be used) is always determined by where
# it is assigned in your source code and has nothing to do with which functions call which.

# In fact variables may be assigned in three different places, corresponding to three different
# scopes:
# • If a variable is assigned outside all def s, it is GLOBAL to the entire file.
# • If a variable is assigned inside a def , it is LOCAL to that function.
# • If a variable is assigned in an enclosing def , it is NONLOCAL to nested functions.

# Example

X = 5  # global variable


def f(a):
    Z = '***hello***'  # local variable
    print(Z)
    print('function locals')
    print(locals())
    return a + Z


print(X)
print()

print(f('Jon'))
print()

print('globals')
print(globals())
print()

# Global names: X , f
# Local Names: a, Z

# The global Statement

# global allows us to change names that live outside a def at the top level of a module file. As
# we’ll see later, the nonlocal statement is almost identical but applies to names in the enclosing
# def ’s local scope, rather than names in the enclosing module. The global statement consists of
# the keyword global , followed by one or more names separated by commas. All the listed names will
# be mapped to the enclosing module’s scope when assigned or referenced within the function body.


# Example

# without global
x, y = 5, 6  # Global x, y

print(f'x={x}, y={y}')


def f(a):
    x, y = 20, 10  # local x, y
    return a * x + y


print(f(2))
print(f'x={x}, y={y}')  # we did not change x, y

# with global
x, y = 5, 6  # Global x, y

print(f'x={x}, y={y}')


def f(a):
    global x, y  # Global x, y: outside def
    x, y = 20, 10
    return a * x + y


print(f(2))
print(f'x={x}, y={y}')  # we changed x, y to 20 and 10 respectively

# Example

x, y = 5, 6  # Global x, y

print(f'x={x}, y={y}')


def f():
    global z  # Declare globals assigned
    z = 0.5
    return z * x + y


print(f())
print(f'x={x}, y={y}, z={z}')

# Notice that x and x are not declared global; Python finds them in the module automatically with
# the following rule.

# Name references search at most four scopes:
# 1 - local,
# 2 - then enclosing functions (if any),
# 3 - then global,
# 4 - then built-in.

# Please note that the following syntax is wrong for Python:

# x = 10
# def f(a):
#     x = 5
#     global x
#     x = x * 2
#     return a

# This is wrong, because we defining x inside a function as a local (x = 5) and then we declare the
# same x as a global and want to change somehow. This is not possible in Python.


# Nested Functions

# Here is what an enclosing function (nested functions) scope looks like:

x = 5  # # Global scope name: not used


def f_1():
    x = 7  # Enclosing def local

    def f_2():
        print(x)  # Reference made in nested def (second part of the rule described above)

    f_2()
    return x ** 2


print(f_1())  # Prints 7 and 49: enclosing def local


# First off, this is legal Python code: the def is simply an executable statement, which can appear
# anywhere any other statement can—including nested in another def . Here, the nested def runs
# while a call to the function f_1 is running; it generates a function and assigns it to the name
# f_2, a local variable within f_1 ’s local scope. In a sense, f_2 is a temporary function that
# lives only during the execution of (and is visible only to code in) the enclosing f_1 .

# The nonlocal statement for Nested Functions

# Nonlocal variable are used in nested function whose local scope is not defined. This means, the
# variable can be neither in the local nor the global scope.

def f_1():
    z = 1

    def f_2():
        nonlocal z

        z = 2

    f_2()
    return z ** 2


print(f_1())  # it prints 4


# In the above code there is a nested function f_2 . The f_2 function is defined in the scope of
# another function f_1 . In the function f_2 we want to change the variable z, which is not a
# global one and not a local one for f_2 itself. Python allows to change it by using nonlocal
# keyword.


# *************************************Part 3: *args, **kwargs*************************************

# In this part we will investigate argument passing—the way that objects are sent to functions as
# inputs. When calling a function, you need to pass arguments to parameters. There are two kinds of
# arguments: positional arguments and keyword arguments.


# Positional arguments

# Using positional arguments requires that the arguments be passed in the same order as their
# respective parameters in the function header.

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

#  Keyword arguments

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


# Special Argument-Matching Modes

# As we’ve just seen, arguments are always passed by assignment in Python; names in the def header
# are assigned to passed-in objects. On top of this model, though, Python provides additional tools
# that alter the way the argument objects in a call are matched with argument names in the header
# prior to assignment. These tools are all optional, but they allow us to write functions that
# support more flexible calling patterns, and you may encounter some libraries that require them.

# By default, arguments are matched by position, from left to right, and you must pass exactly as
# many arguments as there are argument names in the function header. However, you can also specify
# matching by name, provide default values, and use collectors for extra arguments.


# Argument Matching Syntax

# Syntax                  Location  Interpretation

# def func(name)          Function  Normal argument: matches any passed value by position or name
# func(value)             Caller    Normal argument: matched by position

# def func(name=value)    Function  Default argument value, if not passed in the call
# func(name=value)        Caller    Keyword argument: matched by name

# def func(*name)         Function  Matches and collects remaining positional arguments in a tuple
# func(*iterable)         Caller    Pass all objects in iterable as individual positional arguments

# def func(**name)        Function  Matches and collects remaining keyword arguments in a dictionary
# func(**dict)            Caller    Pass all key/value pairs in dict as individual keyword arguments

# def func(*other, name)  Function  Arguments that must be passed by keyword only in calls (3.X)

# def func(*, name=value) Function  Arguments that must be passed by keyword only in calls (3.X)


# Examples


# 1:
# def func(name)
# func(value)
def f(x):
    return x ** 2


print(f(2))


# 2
# def func(name=value)
# func(name=value)
def f(x=2):
    return x ** 2


print(f())
print(f(x=3))


# 3
# def func(*name)
# func(*iterable)
def f(*args):
    print(args)  # in this case args will be tuple
    print(type(args))
    return sum(args)


print(f(1, 2, 0, 4))
print(f(*[1, 2, 0, 4]))


# 4
# def func(**name)
# func(**dict)
def f(**name):
    print(name)  # in this case name will be dict
    print(type(name))
    return sum(name.values())


print(f(**{'a': 3, 'b': 5, 'c': 4}))
print(f(a=3, b=5, c=4))


# 5
#  def func(*other, name)
def f(*args, name):
    print(args, name)
    return sum(args) * name


print(f(1, 2, 3, name=5))
try:
    print(f(1, 2, 3, 5))
except TypeError as e:
    print(e)


# 6
# def func(*, name=value)
def f(*args, name=5):
    print(args, name)
    return sum(args) * name


print(f(1, 2, 3))


# 7
# Keyword-Only Arguments
# Python 3.X generalizes the ordering rules in function headers to allow us to specify keyword-only
# arguments—arguments that must be passed by keyword only and will never be filled in by a
# positional argument. This is useful if we want a function to both process any number of arguments
# and accept possibly optional configuration options.
def f(a, *args, b, c):
    print(a, args, b, c)
    return sum((a, *args, b, c))


print(f(1, 2, 3, 4, b=5, c=78))


# ***************************************Part 4: Final Notes***************************************

# Immutable vs Mutable arguments

# • Arguments are passed by automatically assigning objects to local variable names.
# Function arguments—references to (possibly) shared objects sent by the caller—are just another
# instance of Python assignment at work. Because references are implemented as pointers, all
# arguments are, in effect, passed by pointer. Objects passed as arguments are never
# automatically copied. So be aware, when passing mutable objects to functions.

# • Immutable arguments are effectively passed “by value.”
# • Mutable arguments are effectively passed “by pointer.”

# Example

# passing a list
def f(a):
    a.append(5)
    return a


x = [1, 2, 3]
print(f(x))
print(x)


# passing a string
def f(a):
    a += ' hello'
    return a


x = 'Jon'
print(f(x))
print(x)


# Recursion

def calc_factorial(n):
    if not isinstance(n, int):
        raise TypeError('n should be int')

    if not n >= 0:
        raise ValueError('n should be 0 or positive')

    if n == 0 or n == 1:
        return 1
    else:
        return n * calc_factorial(n - 1)


print(calc_factorial(5))

# Advantages of Recursion
# - Recursive functions make the code look clean and elegant.
# - A complex task can be broken down into simpler sub-problems using recursion.
# - Sequence generation is easier with recursion than using some nested iteration.

# Disadvantages of Recursion
# - Sometimes the logic behind recursion is hard to follow through.
# - Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
# - Recursive functions are hard to debug.


# General guidelines for functional programming:

# • Coupling: use arguments for inputs and return for outputs.
# • Coupling: use global variables only when truly necessary.
# • Coupling: don’t change mutable arguments unless the caller expects it.
# • Cohesion: each function should have a single, unified purpose.
# • Size: each function should be relatively small.
# • Coupling: avoid changing variables in another module file directly.


# TODO: add one more lecture file with the following content:
# TODO: 1. functions as first class objects (passing function to another function as an argument
# TODO:    adding attributes)
# TODO: 2. anonymous functions: lambda
# TODO: 3. functional programming tools (map, filter, reduce)
