# ***************************************Conditional Statements************************************

# We’ll start by looking at the most basic type of if statement.
# In its simplest form, it looks like this:

# if expression:
#   statement

# expression is evaluated in Boolean context and if it is True, the statement is executed,
# if expression is False, then the statement is skipped.


x, y = 0, 5

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

if 'Barcelona' in ('Celta', 'Betis', 'Real Madrid'):
    print('Yes')

# In all the examples shown above, each if expr: has been followed by only a single statement.
# There needs to be some way to say “If expression is True, do all of the following things.”.
# The usual approach taken by most programming languages is to define a syntactic device that
# groups multiple statements into one compound statement or block.

if 'Mars' in ('Venus', 'Earth', 'Mercury'):
    print('Expression is True')
    print('Executing statement')
    print('Done.')
print('After conditional')

# After conditional

# Conditional blocks can be nested to arbitrary depth. Each indent defines a new block,
# and each outdent ends the preceding block.


if 'Mars' in ('Venus', 'Earth', 'Mercury', 'Mars'):
    print('Outer condition is True')
    if 10 < 20:
        print('Inner condition 1')
    print('Between inner conditions')
    if 7:
        print('Inner condition 2')
    print('End of outer condition')
print('After outer condition')

# ******************************The else and elif Clauses******************************************

# Sometimes, you want to evaluate a condition and take one path if it is True but specify
# an alternative path if it is not. This is accomplished with an else clause:

# if expression:
#   statement (1)
# else:
#   statement (2)

# If expression is True, the first statement is executed, and the second is skipped.
# If expression is False, the first statement is skipped and the second is executed without any
# other additional check.

x = 20

if x < 50:
    print('first statement')
    print(f'{x} is smaller than 50')
else:
    print('second statement')
    print(f'{x} is bigger than 50')

# There is also syntax for branching execution based on several alternatives.
# For this, use one or more elif (short for else if) clauses.
# Python evaluates each expression in turn and executes the statement corresponding to the first
# that is True. If none of the expressions are True, and an else clause is specified,
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

# One-Line if Statements

# It is permissible to write an entire if statement on one line.

if 'f' in 'foo':
    print('1')

# is equivalent to, which is not a good idea
if 'f' in 'foo': print('1')

# There can even be more than one statement on the same line, separated by semicolons:
if 'f' in 'foo': print('1'); print('2'); print('3')

# While all of this works, and the interpreter allows it, it is generally discouraged on the
# grounds that it leads to poor readability, particularly for complex if statements.
# PEP 8 specifically recommends against it.

# Python supports one additional decision-making entity called a conditional expression.

# Syntax:  statement_1 if conditional_expression else statement_2
# You could use a standard if statement with an else clause:

age = 12
if age < 21:
    output = 'minor'
else:
    output = 'adult'
print(output)

# But a conditional expression is shorter and arguably more readable as well:
output = 'minor' if age < 21 else 'adult'
print(output)

raining = False
print("Let's go to the", 'beach' if not raining else 'library')

x, y = 40, 56
z = 1 + x if x > y else y + 2
print(z)

# Occasionally, you may find that you want to write what is called a code stub:
# a placeholder for where you will eventually put a block of code that you haven’t implemented yet.

if True:
    pass

# The pass statement solves this problem in Python. It does n’t change program behavior at all.
# It is used as a placeholder to keep the interpreter happy in any situation where a statement
# is syntactically required, but you don’t really want to do anything:

# **************************************looping in python******************************************

# There are two types of loops in Python, for and while.
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary,
# a set, or a string) and traditionally used when you have a block of code which you want to repeat
# a fixed number of times. The Python for statement iterates over the members of a sequence in
# order, executing the block each time.

# ******************************************for loop***********************************************

# Syntax:
# for var in sequence:
#   statement


fruits = ['apple', 'pear', 'mango', 'melon']
for fruit in fruits:
    print(fruit)

# This loop can be described entirely in terms of the concepts you have just learned about.
# To carry out the iteration this for loop describes, Python does the following:

# 1. Calls iter() to obtain an iterator for fruits
# 2. Calls next() repeatedly to obtain each item from the iterator in turn
# 3. Terminates the loop when next() raises the StopIteration exception

# Looping through a String. Loop through the letters in the word "banana":
for letter in "banana":
    print(letter)

# Looping with the range() function. To loop through a set of code a specified number of times,
# we can use the range() function. The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for num in range(6):
    print(num)

# Looping over a dictionary
# You saw earlier that an iterator can be obtained from a dictionary with iter(),
# so you know dictionaries must be iterable. What happens when you loop through a dictionary?
my_dict = {'Python': 1, 'R': 2, 'Matlab': 3}
for key in my_dict.keys():
    print(key)

# As you can see, when a for loop iterates through a dictionary, the loop variable
# is assigned to the dictionary’s keys.

# Nested Loops. A nested loop is a loop inside a loop. The "inner loop" will be executed one
# time for each iteration of the "outer loop":

adjective = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for adj in adjective:
    for fruit in fruits:
        print(adj, fruit)

# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

# The else clause.  The else clause will be executed if the loop terminates
# through exhaustion of the iterable and is not broken by a break statement:

for fruit in ['apple', 'pear', 'mango', 'melon']:
    print(fruit)
else:
    print('Done!')

# *******************************************while loop********************************************

# With the while loop we can execute a set of statements as long as a condition is True.

# Syntax:
# while expression:
#   statement (will be executed until expression becomes False)

# Statement represents the block to be repeatedly executed, often referred to as the body of the
# loop. This is denoted with indentation, just as in an if statement.

# When a while loop is encountered, <expression> is first evaluated in Boolean context.
# If it is True, the loop body is executed. Then <expression> is checked again, and if still True,
# the body is executed again. This continues until <expression> becomes False, at which point
# program execution proceeds to the first statement beyond the loop body.

# Example 1:

value = 1
while value < 6:
    print(value)
    value = value + 1

# Example 2:

# Here’s another while loop involving a list, rather than a numeric comparison:
players = ['Totti', 'Bergkamp', 'Henry', 'Indzaghi']
while players:
    print(players.pop(-1))

# Once all the items have been removed with the .pop() method and the list is empty,
# players is False, and the loop terminates.

# Example 3:

# Infinite Loops. Suppose you write a while loop that theoretically never ends.
while True:
    print('This will never stop!')
    break  # The break is written here to reach the further code.

# Example 4:
# Nested while loops. Similarly to python control structures that can be nested
# within one another, a while loop can be contained within another while loop, as shown here:

fruits = ['apple', 'pear', 'melon', '']
while len(fruits):
    print(fruits.pop(0))
    veggies = ['cucumber', 'tomato', 'onion']
    while len(veggies):
        print('>', veggies.pop(0))

# Example 5: One-Line while Loops
# As with an if statement, a while loop can be specified on one line. If there are multiple
# statements in the block that makes up the loop body, they can be separated by semicolons (;):

number = 5
while number > 0: number -= 1; print(number)

# Example 6: The else Clause. The else clause will be executed if the loop terminates
# through exhaustion of the iterable and is not broken by a break statement:

number = 5
while number > 0:
    number -= 1
    print(number)
else:
    print('Loop done.')

# ********************************Interruption of Loop Iteration***********************************

# In each example you have seen so far, the entire body of the loops is executed on each
# iteration. Python provides two keywords that terminate a loop iteration prematurely:

# break: immediately terminates a loop entirely. Program execution proceeds to the first statement
# following the loop body.

# continue: immediately terminates the current loop iteration. Execution jumps to the top of the
# loop, and the controlling expression is re-evaluated to determine whether the loop
# will execute again or terminate.

# Example 1:

for num in range(1, 10):
    if num % 5 == 0:
        break
    print(num)

# Example 2:

number = 5
while number > 0:
    number -= 1
    if number == 2:
        break
    print(number)
print('Loop ended')

# Example 3:

number = 5
while number > 0:
    number -= 1
    if number == 2:
        continue  # Will skip the iteration at this point.
    print(number)
print('Loop ended.')

# Example 4:

for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
