# # l ol

# x = 1  # int
# y = 2.5  # float
# name = 'John Cena'  # string
# is_cool = True  # capital for boolean

# # Multiple assignment
# x, y, name, is_cool = (1, 2.5, 'John Cena', True)

# # Basic Math
# a = x+y

# # conversions
# x = str(x)  # x is now a string
# y = int(y)  # y is now an integer of 2, not float
# z = float(y)  # y is now a float = 2.0


# # STRINGS
# name = 'Brad'
# age = 37

# # Concatenate
# # can only concatenate of the same data type
# # print('Hello, my name is ' + name + 'and I am' + str(age))

# # interpolatation
# # print('my name is {name} and I am {age}'.format(name=name, age=age))

# # f-strings(only 3.6 + version)
# # much more efficient than above
# # print(f'Hello my name is {name} and I am {age}')

# # String methods
# s = 'hello world'

# # will capitalize first letter
# print(s.capitalize())

# # will make all uppercase letters
# print(s.upper())

# # make all lowercase
# print(s.lower())

# # swap cases
# print(s.swapcase())

# # get length - any data type
# print(len(s))

# # # replace
# # print(s.replace('world', 'everyone'))

# # # counts how many of something in another thing
# # # here counts how many h's in the s string
# # sub = 'h'
# # print(s.count(sub))

# # # starts with - returns boolean
# # print(s.startswith('hello'))

# # # ends with
# # print(s.endswith('d'))

# # # split - same as javascript
# # print(s.split())

# # # find position of first
# # print(s.find('r'))


# # LISTS = array

# # create a list
# numbers = [1, 2, 3, 4, 5]
# numbers2 = list((1, 2, 3, 4, 5))


# # # get a value
# # print(numbers[1])

# # # get length
# # print(len(numbers2))

# # append to list
# # numbers.append(6)
# # print(numbers)

# # remove from list
# # numbers.remove(2)

# # insert into position
# # index, inserted thing
# numbers.insert(2, 'inserted thing')

# # remove at position 4
# numbers.pop(4)

# # reverse
# numbers.reverse()

# # sort
# numbers.sort()

# # reverse sort
# numbers.sort(reverse=true)

# # change value
# numbers[0] = 'lol'


# TUPLE
# A Tuple is a colelction which is ordered and unchangeable. allows duplicate members

# create tuple
# for a tuple use parethesis
fruits = ('apples', 'oranges', 'grapes')
fruits2 = tuple(('apples', 'oranges', 'grapes'))

# if only one element, give ita trailing comma, without it it will be considered a string, not a tuple
fruits3 = ('apples',)

# getting value works
# print(fruits[1])

# cant change a value however, this will give you an error
# fruits[1] = 'peaches'

# you can delete a tuple
del fruits2

# SETS
# set is a collection which is unordered and unindexed, NO DUPLICATES

# create set with curly braces

fruits_set = {'apples', 'oranges', 'mangoes'}

# check if in set - boolean
# print('apples' in fruits_set)

# add to set
# fruits_set.add('grapes')

# remove set
# fruits_set.remove('grapes')

# clear set
# fruits_set.clear()

# delete3
# del fruits_set


# DICTIONARIES - similar to object in javascript or hash in ruby

# create dictionary, keys have quotes

person = {'first_name': 'john', "last_name": 'doe', 'age': 5}

# get value
print(person["first_name"])
print(person.get('last_name'))

# add key-value
person['phone'] = '3013412411'

# get dictionary keys
print(person.keys())
