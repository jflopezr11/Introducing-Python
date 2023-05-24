#Chapter 6  Loop with while and for

#6.1 Repeat with while

count = 1
while count <=5: 
    print(count)
    count += 1

#for me to understand this variable count is 1  now while count is less than or equal to 5 it will print count then add 1 to count and it will continue until count equals 5; however, this does mean that it will increment from 5 to 6 but it will stop because that count will be false. 

#6.1b Cancel with break
# while True: 
#     stuff = input("string to capitalize[tupe q to quit]: ")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())

#"If you want to loop until something occurs, but you're not sure when that might happen, you can use an infinite loop with a break statment" (Lubanovic, 2019, p. 88)

#6.1d Check break Use with else - using while with no break but using an optional else

numbers = [1,3,5]
position = 0

while position < len(numbers): 
    number = numbers[position]
    if number % 2 == 0: 
        print('found even number', number)
        break
    position += 1
else: #break not called
    print('No even number found')


#6.2 Iterate with for and in
#base of experience - string iteration seems like its a common interview topic; however, I've  never done any sting iteration in a work setting. 

word = 'thud'
offset = 0
while offset < len(word): 
    print(word[offset])
    offset += 1

# but this can be done differently 

for letter in word: 
    print(letter)

# cancel with break

word2 = 'thud'
for letter in word2: 
    if letter == 'u': 
        break
    print(letter)


#check break Use with else

#just like 'while', 'for' also has an optional else that checks wherther the 'for' completed normally. if break was not called, the else statement is run. 

word = 'thud'
for letter in word: 
    if letter == 'x':
        print("Eek! And 'x'")
        break
    print(letter)
else: 
    print("No 'x' in there.")



#6.3 Generate Number Sequences with range()
for x in range(0,3): 
    print(x)

#6.1 Use a for loop to print the values of the list [3,2,1,0]

new_list = [3,2,1,0]

for number in new_list:
    print(number)

#6.2 Assign the value 7 to the variable guess_me, and the value 1 to the variable number. Write a while loop that compares number with guess_me. Print 'too low' if number is less than guess_me.
# If number equals guess_me, print "found it!" and then exit the loop. if number is greater than guess_me, print 'opps' and then exit the loop. Increment number at the end of the loop. 

guess_me = 7
number = 1

while True: 
    if number < guess_me:
      print('too low')
      print(number) #added this because I would like to see my loop work. 
    elif number == guess_me:
        print("found it!")
        break
    elif number > guess_me: 
        print("opps!")
        break
    number+=1 

#6.3 Assign the value 5 to the variable guess_me. Use a for loop to iterate a variable called number over range(10). if number is less than guess_me, print 'too low'. if it equals guess_me, print "found it!" and then break out of the for loop. 
#if number is greater than gues_me, print "opps" and then exit the loop. 

guess_me_two = 5

for number in range(10): 
    if number < guess_me_two: 
        print("too low!")
    elif number == guess_me_two: 
        print('found it!')
        break
    else: 
        print("oops!")