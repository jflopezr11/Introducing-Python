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

if color == "red":
    print("It's a tomato")
elif color == 'green':
    print("it's a green bellpepper")
elif color == "bee purple": 
    print("I don't know what it is, but only bees can see it")
else: 
    print("I've never heard of the color", color)


