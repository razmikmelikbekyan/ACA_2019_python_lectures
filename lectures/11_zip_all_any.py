# **********************************************zip************************************************

# The purpose of zip() class is to map the similar index of multiple containers
# so that they can be used just using as single entity.

# Syntax: zip(*iterators)
# Parameters:
# Python iterables or containers ( list, string etc )

# Return value:
# Returns a single iterator object, having mapped values from all the containers.

# The zip() will only iterate over the smallest list passed. If given lists of different
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
