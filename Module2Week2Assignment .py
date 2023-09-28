'''
1. Strings

a. Using string indexing, write two ways to get the character "P" from the string  "Python Programming"

'''
new_string = 'Python Programming'
print(new_string[0])
print(new_string[-0])

'''
b. With string slice notation, extract the word "Programming" from the string  "Python Programming"
'''
x = new_string[7:18]
print(x)

'''
2. String Methods

For all of the questions below, assume the following:
'''

s = "Python Programming"

#a. Using string methods and the string s, write an expression to replace the substring "Programming" with "Software Development".

new_string_p = s.replace('Programming', 'Software Development')
print(new_string_p)
#b. What method can you use to verify that string s begins with the string "Python"?
finding_python = s.find("Python")
print(finding_python)

#c. What method can you use to convert string s to all uppercase?
all_upper = s.upper()
print(all_upper)
#d. Using operators and/or methods, write at least two different expressions to verify that the word "Python" appears in string s

finding_python_two = s.startswith('Python')
print(finding_python_two)

#e. Write an expression to count the number of times the letter n appears in string s
number_of_n = s.count("n"); 
print(number_of_n)

#(Original Lists questions #3 and #4 moved to assignment #3)

#3. String Methods and Conditionals

'''
Using the input() function, read a string from the keyboard. Then using if/elif statements, print out the following messages based on the contents of the string you inputted:

Input	Message
uppercase letters only	"Uppercase"
lowercase letters only	"Lowercase"
letters only (mixed uppercase and lowercase)	"Letters"
numbers only	"Numbers"
whitespace only	"Spaces"
other	"Other"
'''
print("Enter some text")
the_text = input()

if the_text.isupper():
 print("Uppercase")
elif the_text.islower():
    print("lowercase")
elif the_text.isalpha(): 
   print("Letters")
elif the_text.isnumeric(): 
   print("numbers")
elif the_text.isspace(): 
   print("spaces")
else : 
 print("Other")
   

'''
4. String Formatting

There are three players in a game. Their names and scores are listed below as variables and values respectively: 
'''

abe = 10
bea = 12
cecil = 5

#Write an f-string to display the total and the average of the scores. The output should look something like the following:
#Total Score: 27 Average Score: 9.0

total_score = abe + bea + cecil 
average_score = total_score/ 3
print(average_score)

print(f"Total Score: {total_score} Average_score: {average_score}")