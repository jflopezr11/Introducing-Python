'''
1. Lists 

Using only slices, del and/or the assignment operator, change the following list from

[1, 2, 3, 4, 5, 6, 7, 8]

To:

[2, 4, 6, 8, 10, 12]
'''

the_list = [1, 2, 3, 4, 5, 6, 7, 8]

del the_list[0]
del the_list[-2]
del the_list[-3]
del the_list[-4]

the_list += [10, 12]
#print(the_list)


 
'''
2. List Methods

Using only the append, extend, insert and/or remove methods, change the following list from

[1, 2, 3, 4, 5, 6, 7, 8]


To:

[2, 4, 6, 8, 10, 12]

'''
other_list = [1, 2, 3, 4, 5, 6, 7, 8]

other_list.remove(1)
other_list.remove(3)
other_list.remove(5)
other_list.remove(7)
other_list.append(10)
other_list.append(12)
#print(other_list)

 

#Loops

#3. Write a ​for​ loop that will multiply all the numbers of a list together. Assume all of the items in the list are numbers.

newer_list = [1,2,3]
result = 1
for i in newer_list: 
    result = i * result
   # print(result)
 
#4. Write a while loop that will print items from a list of strings. If a string is equal to 'end', 'quit' or 'exit', it should exit from the loop.

the_new_list = ['hello', 'end', 'new', 'exit', 'true', 'quit']
i = 0 
while i < len(the_new_list): 
    s = the_new_list[i]
    if s in ['end', 'quit', 'exit']:
        break
    i = i + 1
    print(s)
 
'''
5. Given the following list:

mylist = [1, 20, 33, 42, 54, 66, 81, 101]

Write code to a list of only the odd numbers
Write code to count the number of odd numbers
Write code to count the total size mylist
Print the percentage of odd numbers in the list. This should be an integer between 0 and 100 (Hint: use round() or int() to convert a float to an integer)
'''
#write code to a list of only the odd numbers

mylist = [1, 20, 33, 42, 54, 66, 81, 101]
odds = []
'''
for i in mylist: 
    if i % 2 == 1 :
        odds.append(i)
    print(odds)
'''
# Write code to count the number of odd numbers

for j in mylist: 
    if j % 2 == 1 :
        odds.append(j)
    print(odds)
    print(len(odds))

# Write code to count the total size mylist
count = 0 

for x in mylist:
    count = count+1

print(count)


#Print the percentage of odd numbers in the list. This should be an integer between 0 and 100 (Hint: use round() or int() to convert a float to an integer)
print(round(len(odds) / len(mylist) * 100, 0)) 

