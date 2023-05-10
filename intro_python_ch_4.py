#Introducing Python Chapter 4

#4.1 Continuing with "\"
# Here I am adding to 'sum1' each line. 
sum1 = 0 
sum1 +=1 
sum1 +=2 

print(sum1)

#Here I can use '\' to continue without calling the variable each line

sum2 = 0 + \
        1 + \
        2 + \
        3

print(sum2)

#4.2 Compare with if, elif, and else

disaster = True
if disaster: 
    print("WOE!")
else: 
    print("Whee!")



furry = False
large = False

#4.2a
#For me to understand this I have nested ifs in here - both variables are True so if it's furry and it's large => "it's a yeti"
#if furry is true but large is false => "cat maybe"
#if furry is false but large is TRUE => "It's something big that has no fur"
#if furry is false and large is false => "It could be a human or a hairless cat"

if furry: 
    if large: 
        print("It's a yeti")
    else:
        print("cat maybe?")
else: 
    if large: 
        print("It's something big that has no fur")
    else:
        print("It could be a human or a hairless cat")



#4.2b elif 

color = "mauve"

if color == "red": # since color is not red it skips this line
    print("It's a tomato")
elif color == 'green': #since color is not green it skips this line
    print("it's a green bellpepper")
elif color == "bee purple": #since color is not bee purple it skips this line
    print("I don't know what it is, but only bees can see it")
else: #since this color is neither of the above this line will run. 
    print("I've never heard of the color", color)


#4.3 truthiness and falsiness

some_list = []
if some_list:  # this didn't run because some_list is an empty list
    print("there's something in here")
else: 
    print("Hey! it's empty")


#4.4 in 

vowels = 'aeiou'
letter = 'o'

print(letter in vowels) # True  - 'o' is in vowels

#4.5 Walrus operator aka  'assignment expression operator'  from https://towardsdatascience.com/the-walrus-operator-in-python-a315e4f84583 - 'An expression evaluates to a value. A statement does something.'

#name:= expr  
#expr is evaluated and then assigned to the variable name. That value will also be returned. 
print(walrus := False) #prints false


#things to do
#1. Choose a number between 1 and 10 and assign it to the variable secret. then, select another number between 1 and 10 and assign it to the variable guess, Next, write the conditional tests to print the string 'too low if guess is less than secret, 'too high' if greater than secret, and 'just right' if equal to secret. 

secret = 4
guess = 5

if guess < secret: 
    print('too low')
elif guess > secret: 
    print('too high')
elif guess == secret: 
    print('just right')
else: 
    print('did you guess?')


#2 Assign True or False to the variables small and green. Write some if/else statements to print which of the mathces those choices: cherry, pea, watermelon, pumpkin. 

small = True
green = False

if small: 
    if green: 
        print("it's probably a pea")
    else:
        print("it's probably a cherry")
else: 
    if green: 
        print('its probably a watermelon')
    else: 
        print("it's probably a pumpkin")







