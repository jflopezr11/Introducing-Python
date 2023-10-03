'''
mylist = ["a", "b", "c", "d", "e"]
print(mylist[1])

mylist2 = ["a", "b", "c", "d", "e"]
print(mylist2[2:4])

mylist3 = [ "a", "b", "c", "d", "e" ]
del mylist3[2]
print(mylist3)

mylist4 = [ "a", "b", "c", "d", "e" ]
mylist4.append('f')
print(mylist4)

mylist5 = ["a", "b", "c", "d", "e"]
mylist5[4] = "f"

print(mylist5)

mylist6 = ["a", "b", "c", "d", "e"]

" ".join(mylist6)

print(mylist6)

mylist7 = [1, 3, 5, 7, 9]

for i in mylist7: 
    print(i)
    if i > 5:
        print(i) 
        break
'''


mylist = [10, 20, 40, 80, 160]
total = 0
for num in mylist:
    total = total + 1
    print(total)  



bicycles = ["bmx", "classical", "dirt"]
color = 'black'
gears = 4

statement = f'''
    My first bicycle was a {bicycles[0]}
    It was the color {color}
    and has {gears} gears.
'''
print(statement)