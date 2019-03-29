# download python from their website
# the extension for a file is .py
# to print something to the console use print()
#ex: print('hello world')


# x = 1  # int
# y = 2.5  # float
# name = 'John Cena'  # string
# is_cool = True  # capital for boolean

# # Multiple assignment
# x, y, name, is_cool = (1, 2.5, 'John Cena', True)

# Basic Math
# a = x+y

# # # conversions
# # x = str(x)  # x is now a string
# # y = int(y)  # y is now an integer of 2, not float
# # z = float(y)  # y is now a float = 2.0


# # # STRINGS
# # name = 'Brad'
# # age = 37

# # # Concatenate
# # # can only concatenate of the same data type, thus age must be converted to string
# # # print('Hello, my name is ' + name + 'and I am' + str(age))

# # # interpolation
# # # print('my name is {name} and I am {age}'.format(name=name, age=age))

# # # f-strings(only 3.6 + version)
# # # much more efficient than above
# # # print(f'Hello my name is {name} and I am {age}')

# # # String methods
# # s = 'hello world'

# # # will capitalize first letter
# # print(s.capitalize())

# # # will make all uppercase letters
# # print(s.upper())

# # # make all lowercase
# # print(s.lower())

# # # swap cases
# # print(s.swapcase())

# # # get length - any data type
# # print(len(s))

# # # # replace
# # # print(s.replace('world', 'everyone'))

# # # # counts how many of something in another thing
# # # # here counts how many h's in the s variable string
# # # sub = 'h'
# # # print(s.count(sub))

# # # # starts with - returns boolean
# # # print(s.startswith('hello'))

# # # # ends with
# # # print(s.endswith('d'))

# # # # split - same as javascript
# # # print(s.split())

# # # # find first position of something
# # # print(s.find('r'))


# # # LISTS = array

# # # create a list
# # numbers = [1, 2, 3, 4, 5]
# # numbers2 = list((1, 2, 3, 4, 5))


# # # # get a value
# # # print(numbers[1])

# # # # get length
# # # print(len(numbers2))

# # # append to list
# # # numbers.append(6)
# # # print(numbers)

# # # remove from list
# # # numbers.remove(2)

# # # insert into position
# # # index, inserted thing
# # numbers.insert(2, 'inserted thing')

# # # remove at position 4
# # numbers.pop(4)

# # # reverse
# # numbers.reverse()

# # # sort
# # numbers.sort()

# # # reverse sort
# # numbers.sort(reverse=true)

# # # change value
# # numbers[0] = 'lol'


# # TUPLE
# # A Tuple is a colelction which is ordered and unchangeable. allows duplicate members

# # create tuple
# # for a tuple use parethesis
# fruits = ('apples', 'oranges', 'grapes')
# fruits2 = tuple(('apples', 'oranges', 'grapes'))

# # if only one element, give it a trailing comma, without it, it will be considered a string, not a tuple
# fruits3 = ('apples',)

# # getting value works
# # print(fruits[1])

# # cant change a value however, this will give you an error
# # fruits[1] = 'peaches'

# # you can delete a tuple
# del fruits2

# # SETS
# # set is a collection which is unordered and unindexed, NO DUPLICATES

# # create set with curly braces

# fruits_set = {'apples', 'oranges', 'mangoes'}

# # check if in set - boolean
# # print('apples' in fruits_set)

# # add to set
# # fruits_set.add('grapes')

# # remove from set
# # fruits_set.remove('grapes')

# # clear set
# # fruits_set.clear()

# # delete set
# # del fruits_set


# # DICTIONARIES - similar to object in javascript or hash in ruby

# # create dictionary, keys have quotes


person = {'first_name': 'john', "last_name": 'doe', 'age': 5}

# # get value
# print(person["first_name"])
# print(person.get('last_name'))

# # add key-value
# person['phone'] = '3013412411'

# # get dictionary keys
# print(person.keys())

# # copy dictionary
# person2 = person.copy()

# remove an item
# del(person["age"])
# person.pop['phone']

# get length
# print(len(person2))


# list of dictionaries
people = [
    {
        'name': 'martha', 'age': 23
    },
    {
        'name': 'kevin', 'age': 26
    },
    {
        'name': 'bob', 'age': 24
    },

]


# FUNCTIONS
# no curly brackets, we use colons and indentation

# create function - similar to ruby - but use parenthesis and colon after, then indent using tab or space
# no need for end
# def sayHello(name):
#     print(f'Hello {name}')


# # call function
# sayHello('Bobby')

# # default value
# def sayHello(name='sam'):
#     print(f'Hello {name}')


# return values
# def getSum(num1, num2):
#     total = num1 + num2
#     return total


# # this will not print to the console, but in code it does work, so you must wrap it in the print function
# getSum(3, 4)

# # like so
# print(getSum(3, 4))

# # or assign it
# num = getSum(3, 4)
# print(num)


# LAMBDA FUNCTION
# small anonymous function - can take any number of arguments but can only have one expression
# similar to javascript arrow functions

# getSum = lambda num1, num2: num1 + num2


# # CONDITIONALS

# x = 10
# y = 5

# # operators (==, != , >, < , >=, <=)
# # no parenthesis needed, just colon and indentation
# if x > y:
#     print('x is greater')

# # if else
# # if x > y:
# #     print('x is greater')
# # else:
# #     print('y is greater')


# # else if or elif

# # if x > y:
# #     print('x is greater')
# # elif x == y:
# #     print('they are equal')
# # else:
# #     print('y is greater')


# # logical operators (and, or , not)

# if x > 2 and x <= 10:
#     print('something')

# if x > 2 or x <= 10:
#     print('something')

# if not(x == 100):
#     print('something')

# # membership operators (in, not in) - test if something is in something else

# # numbers = [1, 2, 3, 4, 5]

# # if x in numbers:
# #     print('x is in the numbers list')

# # if x not in numbers:
# #     print('x is NOT in the numbers list')


# # identity operators (is, is not) - compare objects, not if they are equal,
# # but if they are actually the same object, with the same memory location

# # if x is y:
# #     print('they are the same thing')


# # LOOPS - can loop over a sequence - list, tuple, set, string

# people = ['john', 'sara', 'susan', 'mark']

# # simple for loop
# for person in people:
#     print(f'current person is {person}')

# # break, continue, break stops the function from running , continue skips the current iteration
# # for person in people:
# #     if person == 'susan':
# #         break
# #     print(f'current person is {person}')

# # for person in people:
# #     if person == 'susan':
# #         continue
# #     print(f'current person is {person}')
# #

# # range - similar to standard for loop
# for i in range(len(people)):
#     print(people[i])

# for i in range(0, 11):
#     print(f'Number: {i}')


# # while

# count = 0

# while count <= 10:
#     print('count is less than 10')
#     count += 1


# MODULES - file containing a set of functions to include in your application,
# this is like gems or libraries, there are core python modules, you can install using pip

# importing core python module

# import datetime
# today = datetime.date.today()
# print(today)

# # you can also deconstruct
# # import date time
# #from datetime import date
# # today = date.today()
# # import time
# # timestamp = time.time()
# # print(timestamp)

# # installing with pip -
# # pip3 install  = installs globally like npm install -G


# # CLASSES
# # create class

# class User:
#     # constructor
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def greeting(self):
#         return f'my name is {self.name}'

#     def has_email(self):
#         return f'my email is {self.email}'


# # initialize user object
# brad = User('Brad', 'brad@gmail.com')
# print(brad.greeting())
# print(brad.has_email())

# # Extend Class - all User methods are now in customer


# class Customer(User):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email


# Joey = Customer('Joey', 'joey@gmail.com')
# print(Joey.greeting())
