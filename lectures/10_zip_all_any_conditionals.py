# **********************************************zip************************************************

# The purpose of zip() is to map the similar index of multiple containers
# so that they can be used just using as single entity.

# Syntax: zip(*iterators)
# Parameters:
# Python iterables or containers ( list, string etc )

# Return value:
# Returns a single iterator object, having mapped values from all the containers.

# The zip() function will only iterate over the smallest list passed. If given lists of different
# lengths, the resulting combination will only be as long as the smallest list passed.

short_list = [4, 5, 6]
long_list = ['four', 'five', 'six', 'seven', 'eight']

print(list(zip(short_list, long_list)))
# [(4, 'four'), (5, 'five'), (6, 'six')]

player_name = ['Ramos', 'Carvajal', 'Kroos', 'Modric', 'Benzema']
player_number = [4, 2, 8, 10, 9]
player_position = ['defender', 'defender', 'midfielder', 'midfielder', 'forward']

mapped = zip(player_name, player_number, player_position)

# To view the results we pass the zip object to list.

mapped = list(mapped)
print(list(mapped))

# [('Ramos', 4, 'defender'), ('Carvajal', 2, 'defender'), ('Kroos', 8, 'midfielder'),
# ('Modric', 10, 'midfielder'), ('Benzema', 9, 'forward')]

# unzipping values

names, numbers, positions = zip(*mapped)
print(list(names))

# ['Ramos', 'Carvajal', 'Kroos', 'Modric', 'Benzema']

# The simplest way to produce a dictionary from 2 lists is with help of zip function.

countries = ['Armenia', 'France', 'Italy', 'Argentina']
rank = [1, 2, 3, 4]
my_dict = dict(zip(countries, rank))

# **********************************************all************************************************

# The all() method returns True when all elements in the given iterable are true.
# If not, it returns False.

# The syntax of all() method is: all(iterable) -> bool

# All values are true -> True
# All values are false -> False
# One value is true (others are false) -> False
# One value is false (others are true) -> False
# Empty iterable -> True

my_list = [1, 3, 4, 5]
print(all(my_list))
# True

my_list = [0, False]
print(all(my_list))
# False

my_list = [0, False, 5]
print(all(my_list))
# False

my_list = []
print(all(my_list))
# True

my_string = 'This is a string'
print(all(my_string))
# True

# In case of dictionaries, if all keys (not values) are true or the dictionary is empty,
# all() returns True. Else, it returns false for all other cases.

my_dict = {0: 'False', 1: 'False'}
print(all(my_dict))
# False

my_dict = {1: 'True', 2: 'True'}
print(all(my_dict))
# True

my_dict = {1: 'True', 'False': 0}
print(all(my_dict))
# True

# **********************************************any************************************************

# The any() method returns True if any element of an iterable is True. If not, any() returns False.

# The syntax of any() method is: any(iterable) -> bool

# All values are true -> True
# All values are false -> False
# One value is true (others are false) -> True
# One value is false (others are true) -> True
# Empty iterable -> False

my_list = [1, 3, 4, 0]
print(any(my_list))
# True

my_list = [0, False]
print(any(my_list))
# False

my_list = [0, False, 5]
print(any(my_list))
# True

my_list = []
print(any(my_list))
# False

my_str = 'This is a string'
print(any(my_str))
# True

my_str = ''
print(any(my_str))
# False

# In case of dictionaries, if all keys (not values) are false, any() returns False.
# If at least one key is true, any() returns True.

my_dict = {0: 'False'}
print(any(my_dict))
# False

my_dict = {0: 'False', 1: 'True'}
print(any(my_dict))
# True

my_dict = {0: 'False', False: 0}
print(any(my_dict))
# False

my_dict = {}
print(any(my_dict))
# False

my_dict = {'0': 'False'}
print(any(my_dict))
# True

# ***************************************Conditional Statements************************************

# We’ll start by looking at the most basic type of if statement.
# In its simplest form, it looks like this:

# if expr:
# statement

# expr is an expression evaluated in Boolean context
# statement is a valid Python statement, which must be indented.

# If expr is true, then statement is executed.
# If expr is false, then statement is skipped over and not executed.

x = 0
y = 5

# In all below written code the evaluated expression is True.

if x < y:
    print('Yes')

if y:
    print('Yes')

if x or y:
    print('Yes')

if 'play' in 'playstation':
    print('yes')

# In all below written code the evaluated expression is False.

if x > y:
    print('Yes')

if x:
    print('Yes')

if x and y:
    print('Yes')

if 'Barcelona' in ['Celta', 'Betis', 'Real Madrid']:
    print('Yes')

# In all the examples shown above, each if expr: has been followed by only a single statement.
# There needs to be some way to say “If expr is true, do all of the following things.”.
# The usual approach taken by most programming languages is to define a syntactic device that
# groups multiple statements into one compound statement or block.

if 'Mars' in ['Venus', 'Earth', 'Mercury']:
    print('Expression is True')
    print('Executing statement')
    print('Done.')
print('After conditional')

# After conditional

# Blocks can be nested to arbitrary depth. Each indent defines a new block,
# and each outdent ends the preceding block.

if 'Mars' in ['Venus', 'Earth', 'Mercury', 'Mars']:
    print('Outer condition is true')
    if 10 > 20:
        print('Inner condition 1')
    print('Between inner conditions')
    if 10 < 20:
        print('Inner condtion 2')
    print('End of outer condition')
print('After outer condition')

# Outer condition is true
# Between inner conditions
# Inner condtion 2
# End of outer condition
# After outer condition

# ******************************The else and elif Clauses******************************************

# Sometimes, you want to evaluate a condition and take one path if it is true but specify
# an alternative path if it is not. This is accomplished with an else clause:

# if expr:
# statement (1)
# else:
# statement (2)

# If expr is true, the first statement is executed, and the second is skipped.
# If expr is false, the first statement is skipped and the second is executed.
# Either way, execution then resumes after the second statement.
# Both statement are defined by indentation, as described above.

x = 20

if x < 50:
    print('first statement')
    print('x is small')
else:
    print('second statement')
    print('x is large')

# first statement
# x is small

# There is also syntax for branching execution based on several alternatives.
# For this, use one or more elif (short for else if) clauses.
# Python evaluates each expr in turn and executes the statement corresponding to the first
# that is true. If none of the expressions are true, and an else clause is specified,
# then its expression is executed:

name = 'Joe'

if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

# Hello Joe

# One-Line if Statements

# It is permissible to write an entire if statement on one line.

if 'f' in 'foo':
    print('1')

# is equivalent to

if 'f' in 'foo': print('1')

# There can even be more than one statement on the same line, separated by semicolons:
if 'f' in 'foo': print('1'); print('2'); print('3')

# While all of this works, and the interpreter allows it, it is generally discouraged on the
# grounds that it leads to poor readability, particularly for complex if statements.
# PEP 8 specifically recommends against it.

# Python supports one additional decision-making entity called a conditional expression.

# Syntax:  expr1 if conditional_expr else expr2
# You could use a standard if statement with an else clause:

age = 12

if age < 21:
    output = 'minor'
else:
    output = 'adult'

# But a conditional expression is shorter and arguably more readable as well:

output = 'minor' if age < 21 else 'adult'

raining = False
print("Let's go to the", 'beach' if not raining else 'library')

x = y = 40
z = 1 + x if x > y else y + 2

# Occasionally, you may find that you want to write what is called a code stub:
# a placeholder for where you will eventually put a block of code that you haven’t implemented yet.

if True:
    pass

# The pass statement solves this problem in Python. It doesn’t change program behavior at all.
# It is used as a placeholder to keep the interpreter happy in any situation where a statement
# is syntactically required, but you don’t really want to do anything:
