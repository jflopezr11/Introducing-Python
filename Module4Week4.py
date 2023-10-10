#1. A school cafeteria has different types of set meals for lunch. A dictionary is used to keep track of the number of set meals by type

lunch = { 'chicken': 7, 'fish': 2, 'beef': 4, 'pork': 3 }


#How would you access the number of chicken dishes?
print(lunch.get('chicken'))
#What happens if you try to access vegan dishes?
print(lunch.get('vegan')) #None
#How would you add a vegan dish entry with a count of 2?
lunch.update({'vegan': 2})
#fish has been added. How would you change the count to 5?
lunch.update({'fish': 5})
print(lunch)
#beef has run out. How would you remove it from the dictionary?
lunch.pop('beef')
print(lunch)

'''
Create a dictionary that has the reverse  key-value relationship of another dictionary. Your code should work for any dictionary of any size. You can assume that the keys and values are unique.

For example, given the following dictionary
'''

x = {'a': 1, 'b':2, 'c':3, 'd':4 }

'''
Your new dictionary will be

{1:'a', 2:'b', 3:'c', 4:'d'}
'''

x_swap = {v: k for k, v in x.items()}
print(x_swap) 


'''
Count each word from a given string and store it in a dictionary. The words should be the keys and counts are the values. Assume that the string contains only lowercase characters and does not contain any punctuations.

For example, given a string


new_dict = {}
count = 0 
the_string = 'a fool thinks himself to be wise but a wise man knows himself to be a fool'

for word in the_string: 
    count += 1 
    new_dict.update(word)

print(new_dict)
'''


#Given the following dictionary of lists of test scores

scores = {'Louis': [92, 95, 94],
          'Pat': [88, 75, 86],
          'Sudha': [93, 90, 96],
          'Zhen': [80, 83, 91] }


#Write code for the following

#print the list of scores for Louis
print(scores['Louis'])

#change Sudha's list of scores to the following: [90, 96, 93]
scores['Sudha'] = [90, 96, 93]

#change one of Pat's score from 75 to 78
scores['Pat'][1] = 78
#print the number of entries in the dictionary (the total number of students)
print(len(scores))

#print Zhen's average test score
zhen = scores['Zhen']
sum  = sum(zhen)
average = sum/ len(zhen)
print(average)



f = open("gettysburg.txt")
lines = f.readlines()

for line in lines:
  print(line)


number_of_words = 0 

for word in lines: 
    number_of_words += len(lines)
    print(number_of_words)

f.close()