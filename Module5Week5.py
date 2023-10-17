

'''
1. Functions

a. Write a function that takes an integer as an argument and returns its factorial.

For example, 4! = factorial(4) = 4 * 3 * 2 * 1 = 24
'''
import math

def my_fact(int):
    print(math.factorial(int))

my_fact(4)
my_fact(5)
my_fact(8)

'''

b. Write a function that accepts a list of numbers in gallons and returns a list of numbers in liters (1 gallon = 3.78541 liters)

For example, if given the following list:

[1, 10, 100, 0.5, 5, 50]

Your function should return:

[3.78541, 37.8541, 378.541, 1.892705, 18.92705, 189.2705]

'''
l_conversion = 3.78541 


def gallons_to_liters(list):
    innerlist = []
    for i in list: 
        innerlist.append(i * l_conversion)
    print(innerlist)


gallons_to_liters([1, 10, 100, 0.5, 5, 50])

'''
c. Write a function that accepts a list of strings and keep only strings that are less than 6 characters. 

For example, if given the following list:

['Apple', 'Banana', 'Cherry', 'Durian', 'Eggplant', 'Fig', 'Grape']

Your function should return:

['Apple', 'Fig', 'Grape']
'''
def list_of_strings_only(list): 
    innerList = []
    for string in list: 
        if len(string) < 6: 
            innerList.append(string)
            print(innerList)
        elif len(string) >= 6: 
            print(f"{string} has {len(string)} characters")
    return innerList

fruits = ['Apple', 'Banana', 'Cherry', 'Durian', 'Eggplant', 'Fig', 'Grape']
list_of_strings_only(fruits)


'''
d. Write a function that accepts a list of dictionaries and returns the city name with the highest population.

For example, given the following list of dictionaries by the city key:

[{"city":"San Francisco","population":884363},
{"city":"Berkeley","population":122324},
{"city":"Oakland","population":425195}]

Should return:

"San Francisco"
'''



'''
2. Function Arguments

Write a function that returns a list of numbers in sequence. It has the following options:

if no arguments are passed to the function, return a list of numbers from 0 to 9
if one argument (start) is passed, return a list of numbers from start to start + 10
if two arguments (start, count) are passed, return a list of numbers from start to start + count
Examples:

print(number_list())     # returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(number_list(5))    # returns [5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 
print(number_list(5, 3)) # returns [5, 6, 7]
'''

'''
3. (Optional) Write a function that accepts a string and an optional number (n) as arguments. 

It should return a string in all uppercase if only the string argument is passed of if n is 0.

Otherwise, it should return a string with the first n characters as uppercase and not affect the rest.

(Hint: you may want to review string slices and use the append operator (+))

For example:

upperstring('abcdef') # returns 'ABCDEF'
upperstring('abcdef', 3) # returns 'ABCdef'
upperstring('This is a STRING', 5) # returns 'THIS is a STRING'

'''