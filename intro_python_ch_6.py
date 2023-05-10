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