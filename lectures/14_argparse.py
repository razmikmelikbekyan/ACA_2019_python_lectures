# ***************************************Argument Parser*******************************************

import argparse


# This lecture provides an introduction to argparse, the recommended command-line parsing module in
# the Python standard library.

# Suppose we have the following function:

def calculate(x, y, operation):
    """Makes calculation based on given operation."""
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mul':
        return x * y
    elif operation == 'div':
        return x / y


# We want to use this from command line: by giving arguments from console
# We can do it using by built in input() function, but it is not the best way. For this purpose we
# should use argparse.

# The typical command-line application have the following interface:

"""python [file].py [command] [options] NAME"""

# For example

"""python [file].py 10 20 add"""

# or

"""python [file].py --x=10 --y=20 --operation=add"""

# or

"""python [file].py add --x 10 --y 20"""

# So lets start with the simple example
parser = argparse.ArgumentParser()

if __name__ == '__main__':
    parser.parse_args()

# If we run the following from console:
"""python 14_argparse.py --help"""

# we will get the following message
"""
usage: 14_argparse.py [-h]

optional arguments:
  -h, --help  show this help message and exit
"""

# As seen above, even though we did not specify any help arguments in our script, its still giving
# us a nice help message.

# *********************************Part 1: Positional Arguments************************************

# In this part we will introduce positional arguments.

# Whenever we want to specify which command-line options the program will accept,  we use the
# "add_argument()" method.

parser = argparse.ArgumentParser()
parser.add_argument("x")
parser.add_argument("y")
parser.add_argument("operation")

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)

# If we run the following from console:
"""python 14_argparse.py --help"""

# we will get the following message
"""
usage: 14_argparse.py [-h] x y operation

positional arguments:
  x
  y
  operation

optional arguments:
  -h, --help  show this help message and exit
"""

# If we run the following from console:
"""python 14_argparse.py"""

# we will get the following message
"""
usage: 14_argparse.py [-h] x y operation
14_argparse.py: error: the following arguments are required: x, y, operation
"""

# So we got error, because our code is requires x, y and operation to be given.

# The correct way of running the program is the following:
"""python 14_argparse.py 1 20 add"""

# We will get the following:
"""
Namespace(operation='add', x='1', y='20')
"""

# This is the result of print(args) statement.

# We can add help for each argument.
parser = argparse.ArgumentParser()
parser.add_argument("x", help='The x to be passed calculate function.')
parser.add_argument("y", help='The y to be passed calculate function.')
parser.add_argument("operation", help='The operation to be passed calculate function.')

if __name__ == '__main__':
    args = parser.parse_args()
    print(f'x={args.x}, type of x is: {type(args.x)}')
    print(f'y={args.y}, type of y is: {type(args.y)}')
    print(f'operation={args.operation}, type of operation is: {type(args.operation)}')

# If we run the following from console:
"""python 14_argparse.py --help"""

# we will get the following message
"""
usage: 14_argparse.py [-h] x y operation

positional arguments:
  x           The x to be passed calculate function.
  y           The y to be passed calculate function.
  operation   The operation to be passed calculate function.

optional arguments:
  -h, --help  show this help message and exit
"""

# We can get the given arguments from args by using "args.argument_name", for example: args.x

# If we run the following from console:
"""python 14_argparse.py 1 20 add"""

# We will get the following:
"""
x=1, type of x is: <class 'str'>
y=20, type of y is: <class 'str'>
operation=add, type of operation is: <class 'str'>
"""

# This is the result of followings statements.
# print(f'x={args.x}, type of x is: {type(args.x)}')
# print(f'y={args.y}, type of y is: {type(args.y)}')
# print(f'operation={args.operation}, type of operation is: {type(args.operation)}')

# We see that by default all passed arguments are strings (like for input). But argparse allows to
# specify type of argument.
parser = argparse.ArgumentParser()
parser.add_argument("x", type=float,
                    help='The x to be passed calculate function.')
parser.add_argument("y", type=float,
                    help='The y to be passed calculate function.')
parser.add_argument("operation", type=str,
                    help='The operation to be passed calculate function.')

if __name__ == '__main__':
    args = parser.parse_args()
    print(f'x={args.x}, type of x is: {type(args.x)}')
    print(f'y={args.y}, type of y is: {type(args.y)}')
    print(f'operation={args.operation}, type of operation is: {type(args.operation)}')
    print(f'calculation result={calculate(args.x, args.y, args.operation)}')

# If we run the following from console:
"""python 14_argparse.py 1 20 add"""

# We will get the following:
"""
x=1, type of x is: <class 'float'>
y=20, type of y is: <class 'float'>
operation=add, type of operation is: <class 'str'>
calculation result=21.0
"""

# Please not that order is matters: the passed arguments order must be aligned with the order
# they are defined - x, y, operation.


# **********************************Part 2: Optional Arguments*************************************

# So far we have been playing with positional arguments. Let us have a look on how to add optional
# ones:

parser = argparse.ArgumentParser()
parser.add_argument("x", type=float,
                    help='The x to be passed calculate function.')
parser.add_argument("y", type=float,
                    help='The y to be passed calculate function.')
parser.add_argument("operation", type=str,
                    help='The operation to be passed calculate function.')
parser.add_argument("-v", "--verbose", type=int,
                    help="If 1, prints the result of calculation.")

if __name__ == '__main__':
    args = parser.parse_args()
    result = calculate(args.x, args.y, args.operation)
    if args.verbose == 1:
        print(f'calculation result={result}')

# An optional argument is (by default) given None as a value when its not being passed.
# So if we will not specify it from console, by default args.verbose will be None.

# If we run the following from console:
"""python 14_argparse.py 1 20 add --verbose 1"""
# or
"""python 14_argparse.py 1 20 add -v 1"""

# We will get the following:
"""
calculation result=21.0
"""

# The above example accepts arbitrary integer values for --verbose, but for our simple program,
# only two values are actually useful, "True" or "False". Let’s modify the code accordingly:
parser = argparse.ArgumentParser()
parser.add_argument("x", type=float,
                    help='The x to be passed calculate function.')
parser.add_argument("y", type=float,
                    help='The y to be passed calculate function.')
parser.add_argument("operation", type=str,
                    help='The operation to be passed calculate function.')
parser.add_argument("-v", "--verbose", action='store_true',
                    help="If True, prints the result of calculation.")

if __name__ == '__main__':
    args = parser.parse_args()
    result = calculate(args.x, args.y, args.operation)
    if args.verbose:
        print(f'calculation result={result}')

# The keyword "action" is being given the value "store_true" which means that if the option is
# specified, then assign the value "True" to args.verbose. Not specifying the option implies False.


# If we run the following from console:
"""python 14_argparse.py 1 20 add --verbose"""

# We will get the following:
"""
calculation result=21.0
"""

# ***********************************Part 3: Advanced options**************************************

# In this part we will introduce some advanced possibilities of argparse.


# required

# An argument is made required with the required option.

parser = argparse.ArgumentParser()
parser.add_argument('--name', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    print(f'Hello {args.name}')

"""python 14_argparse.py --name Mark"""
# The example must have the name argument specified; otherwise it fails.


# dest

# The dest option of the add_argument() gives a name to the argument. If not given, it is
# inferred from the option.


parser = argparse.ArgumentParser()
parser.add_argument('--name', required=True, dest='aaaa')

if __name__ == '__main__':
    args = parser.parse_args()
    print(f'Hello {args.aaaa}')
"""python 14_argparse.py --name Mark"""
# The program gives the aaaa name to the --name argument.


# default

# The default option specifies the default value, if the value is not given. (it uses default
# value instead of None).

parser = argparse.ArgumentParser()
parser.add_argument('--name', required=True)
parser.add_argument('--count', default=3, type=int)

if __name__ == '__main__':
    args = parser.parse_args()
    for _ in range(args.count):
        print(f'Hello {args.name}')
"""python 14_argparse.py --name Mark"""
# The count value is not required; if not given, the default will be 3.


# append

# The append action allows to group repeating options.

parser = argparse.ArgumentParser()
parser.add_argument('--name', dest='names', action='append', required=True)
parser.add_argument('--count', default=1, type=int)

if __name__ == '__main__':
    args = parser.parse_args()
    for _ in range(args.count):
        print(type(args.names))
        for x in args.names:
            print(f'Hello {x}')

# """python 14_argparse.py --name Mark --name John --name Bob"""
# The example produces greeting messages to all names specified with the name option; they can be
# repeated multipile times.


# nargs

# The nargs specifies the number of command - line arguments that should be consumed.

parser = argparse.ArgumentParser()
parser.add_argument('--full-name', required=True, nargs=2)

if __name__ == '__main__':
    args = parser.parse_args()
    print(args.full_name)
    print(type(args.full_name))
    name, surname = args.full_name
    print(f'My name is: {name}')
    print(f'My surname name  is: {surname}')

"""python 14_argparse.py --full-name Bob Bobovich"""
# The example shows a name and surname of person. It expects two arguments.

# Variable number of arguments can be set with the * character.
parser = argparse.ArgumentParser()
parser.add_argument('--numbers', required=True, nargs="*", type=float)

if __name__ == '__main__':
    args = parser.parse_args()
    print(f'sum of numbers: {sum(args.numbers)}')

"""python 14_argparse.py --numbers 2.5 3 4 0.5"""
# The example computes the sum of numbers; we can specify variable number of arguments to the
# program.


# choices

# The choices option limits arguments to the given list.

parser = argparse.ArgumentParser()
parser.add_argument("--o", type=str, choices=['add', 'sub', 'mul', 'div'], required=True,
                    help='The operation to be passed calculate function.')
parser.add_argument("--x", type=float, default=1.,
                    help='The x to be passed calculate function.')
parser.add_argument("--y", type=float, default=1.,
                    help='The y to be passed calculate function.')

parser.add_argument("-v", "--verbose", action='store_true',
                    help="If True, prints the result of calculation.")

if __name__ == '__main__':
    args = parser.parse_args()
    result = calculate(args.x, args.y, args.o)
    if args.verbose:
        print(f'calculation result={result}')

"""python 14_argparse.py --o add --x 2 --y 6 --verbose"""
# In the example, the o argument can accept only the following values: add, sub, mul, div.
