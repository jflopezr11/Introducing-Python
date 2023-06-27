# Tuples and List

#create with Commas and ()

#starting off with an empty tuple using (); 

empty_tuple = ()

#if you want a tuple with one or more elements, add a comma following each element 
one_marx = 'Groucho',
print(one_marx)

#you can also enclose them in parentheses and still get the same thing
#Without the comma it isn't a tuple. 
#Tuples let you assign multiple Variables at Once:
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple

print(a)
print(b)
print(c)

#create with tuple()

marx_list = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list)

#iterate with for and in

words = ('fresh', 'out', 'of', 'ideas')

for word in words: 
    print(word)

# modify a tuple
#you can't, like strings, tuples are immutables, so you can't change an existings one but  you can concatenate

t1 = ('fee','fie','foe')
t2 = ('flop',)
t1 + t2 #or t1 +=t2

#List 7.2
#List are good for keeping tracks of things by their order, especially when the order and contents might change. List are mutable 
#create with []

empty_list = []
weekdays = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday']
leap_years = [2000, 2004, 2008]

#create or convert with list()
a_tuple = ('ready', 'fire', 'aim')
list(a_tuple)
print(a_tuple)


#7.1 
years_list = [1991, 1992, 1993, 1994, 1995, 1996]

#7.2
1994

#7.3
1996

#7.4
things = ('mozzarella', 'cinderella', 'salmonella')

##upper_name_in_list = things.captialize(1) 
##print(upper_name_in_list)

#I should get an error

for thing in things: 
    if thing.startswith('c'): 
        things.capitalize(1)
        print(things)

        


