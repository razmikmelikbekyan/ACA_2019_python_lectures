# Comprehensions are constructs that allow sequences to be built from other sequences.
# Python 2.0 introduced list comprehensions and Python 3.0 comes also with
# dictionary and set comprehensions.

# ************************************ List Comprehensions ****************************************

# A list comprehension consists of the following parts:

# 1. An Input Sequence.
# 2. A Variable representing members of the input sequence. In our case the "e" variable.
# 3. An Optional expression. In our case the "isinstance(e, int)" expression
# 4. An Output Expression producing elements of the output list from members of the Input Sequence
# that satisfy the predicate.

input_sequence = [1, '4', 9, 'a', 0, 4]
output = [e ** 2 for e in input_sequence if isinstance(e, int)]
print(output)

# The iterator part iterates through each member e of the input_sequence.
# An optional expression checks if the member is integer.
# If the member is an integer then it is passed to the output expression, squared,
# to become a member of the output list.

# The same code shown with classic for iterator.

input_sequence = [1, '4', 9, 'a', 0, 4]
output = []
for e in input_sequence:
    if isinstance(e, int):
        output.append(e)
print(output)

# Nested List Comprehensions

# Nested List Comprehensions are nothing but a list comprehension within another list comprehension
# which is quite similar to nested for loops. Let's dive into an examples.

# Example 1:

# Suppose we want to create a matrix which looks like below:

# matrix = [[0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4]]

# The below code uses nested for loops for the given task:

matrix = []
for i in range(5):
    matrix.append([])  # Append an empty sublist inside the list
    for j in range(5):
        matrix[i].append(j)
print(matrix)

# The same output can be achieved using nested list comprehension in just one line:

matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

# Example 2:

# The problem from your homework:
# Write a Python program to generate a ​ 3*4*6 3D​ array whose each element is “​ * ​ ”.

# Naive solution
array = []
for _ in range(3):
    temp_1 = []
    for _ in range(4):
        temp_2 = []
        for _ in range(6):
            temp_2.append("*")
        temp_1.append(temp_2)
    array.append(temp_1)

from pprint import pprint

pprint(array)

# Elegant solution
array = [[["*" for _ in range(6)] for _ in range(4)] for _ in range(3)]
pprint(array)

# Example 3:

#  Suppose we want to flatten a given 2-D list:

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# expected_output: flatten_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# This can be done using nested for loops as follows:

nested_matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_matrix = []
for sublist in nested_matrix:
    for val in sublist:
        flatten_matrix.append(val)

# Again this can be done using nested list comprehension which has been shown below:
flatten_matrix = [val for sublist in nested_matrix for val in sublist]
print(flatten_matrix)

# Please note that in this case you should start with the for loop which is the highest,
# then go down sequentially

# Example 4:

# Suppose we want to flatten a given 2-D list and only include those strings
# whose lengths are less than 6:

# planets = [
#     ['Mercury', 'Venus', 'Earth'],
#     ['Mars', 'Jupiter', 'Saturn'],
#     ['Uranus', 'Neptune', 'Pluto']
# ]
# Expected Output: flatten_planets = [‘Venus’, ‘Earth’, ‘Mars’, ‘Pluto’]

# This can be done using an if condition inside a nested for loop which is shown below:

planets = [
    ['Mercury', 'Venus', 'Earth'],
    ['Mars', 'Jupiter', 'Saturn'],
    ['Uranus', 'Neptune', 'Pluto']
]
flatten_planets = []
for sublist in planets:
    for planet in sublist:
        if len(planet) < 6:
            flatten_planets.append(planet)

# This can also be done using nested list comprehensions which has been shown below:
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6]
print(flatten_planets)

# Example 5:

# 2 conditionals inside list comprehension
input_sequence = [1, '4', 9, 'a', 0, 4]
output = [e ** 2 if isinstance(e, int) else e + "_hello" for e in input_sequence]
print(output)

# ********************************** Dict Comprehensions ******************************************

# Like List Comprehension, Python allows dictionary comprehensions.
# We can create dictionaries using simple expressions. A dictionary comprehension takes the form
# {key: value for (key, value) in iterable}. However, not all for loop can be written as a
# dictionary comprehension but all dictionary comprehension can be written with a for loop. Let's
# dive in examples.

# Example 1:

# Here let us use a list of numbers and create a dictionary with string value of the number as key
# and the number as values.

my_list = [1, 2, 3, 4, 5]
my_dictionary = {str(i): i for i in my_list}
print(my_dictionary)

# Example 2:

# Suppose we want to make dictionary from a list using comprehension. As an output we want the
# elements of our list be the keys and their squares as the values for new created dictionary.

my_dictionary = {x: x ** 2 for x in [1, 2, 3, 4, 5]}
print(my_dictionary)

# Example 3:

# Suppose we want to make a dictionary from iterating over a string. We want to match each
# character in our string to it's doubled result.

my_string = 'coding'
my_dictionary = {x: x * 2 for x in my_string}
print(my_dictionary)

# Example 4:

# Let's Initialize the fahrenheit dictionary.
fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}
# Lets get the corresponding celsius values and create the new dictionary
celsius = {k: (5 / 9) * (v - 32) for k, v in fahrenheit.items()}
print(celsius)

# Example 5:

# We can use Dictionary comprehensions with if and else statements and with other expressions too.
# This example below maps the numbers to their cubes that are not divisible by 4:

my_dictionary = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print(my_dictionary)

# Example 6:
# What if we have multiple conditionals? Suppose we have 3 conditions.

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
data_conditional = {
    k: v for (k, v) in data.items() if v > 2 and v % 2 == 0 and v % 3 == 0}
print(data_conditional)

# In a for loop this will correspond to:

data_conditional = {}
for (k, v) in data.items():
    if v >= 2 and v % 2 == 0 and v % 3 == 0:
        data_conditional[k] = v
print(data_conditional)

# Example 7:

# Dealing with an if-else condition is also easy with dictionary comprehension.

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
data_conditional = {k: ('even' if v % 2 == 0 else 'odd') for (k, v) in data.items()}
print(data_conditional)

# Example 8:

# Similarly lists dictionaries can be nested and thus their comprehensions can be nested as well.
# Let's see what this means:

nested_dict = {'first': {'a': 1}, 'second': {'b': 2}}
float_dict = {
    k_1: {k_2: float(v_2) for k_2, v_2 in v_1.items()} for k_1, v_1 in nested_dict.items()
}
print(float_dict)

# The code works with the inner dictionary values and converts them to float and then combines
# the outer keys with the new float inner values into a new dictionary.

# Note that you can rewrite the above code chunk also with a nested for loop:
nested_dict = {'first': {'a': 1}, 'second': {'b': 2}}
float_dict = {}
for k_1, v_1 in nested_dict.items():
    temp = {}
    for k_2, v_2 in v_1.items():
        temp[k_2] = float(v_2)
    float_dict[k_1] = temp
print(float_dict)

# ********************************** Set Comprehensions *******************************************
# Like list and dict comprehensions returns a set based on existing iterables.
# {expression(variable) for variable in input_set [predicate expression]}

# 1. Expression is optional. An output expression producing members of the new set from members
# of the input set that satisfy the predicate expression.

# 2. Variable is required. Variable representing members of an input set.
# 3. Input_set is required. Represents the input set.
# 4. Predicate expression is optional. Acting as a filter on members of the input set.

# Example 1:

my_set = {s for s in [1, 2, 1, 0]}
print(my_set)

my_set = {s ** 2 for s in [1, 2, 1, 0]}
print(my_set)

my_set = {s ** 2 for s in range(10)}
print(my_set)

# Example 2:

# Set comprehension with conditional statement:
my_set = {s for s in [1, 2, 3] if s % 2 != 0}
print(my_set)

# Example 3:

# Nested set comprehension
my_set = {(m, n) for n in range(2) for m in range(3, 5)}
print(my_set)
