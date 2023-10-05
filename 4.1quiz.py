'''
mylist = [ 1, 2, 3, 5, 7, 11 ]

print(mylist.index(7))


mylist2 = [2, 4, 8, 10]

mylist2[3] = 15
print(mylist2)
'''
'''
san_francisco_info = {
    "name": "San Francisco",
    "state": "California",
    "country": "United States",
    "population": 883305
}

san_francisco_info["average_temperature"] = 3

print(san_francisco_info)

new_dict = {"A":100, "B": 200, "C": 300}

new_dict["D"] = 400

print(new_dict)
'''
states = [ {'state': 'California', 'capital': 'Sacramento', 'year_admitted': 1850},
           {'state': 'New York', 'capital': 'Albany', 'year_admitted': 1788},
           {'state': 'Texas', 'capital': 'Austin', 'year_admitted': 1845} ]

print(len(states))
print(len(states[0]))
print(states[2]['capital'])
print(states[0]['year_admitted'])
states[0]['capital'] = 'Merced'
print(states[0]['capital'])

states.append({'state': 'Nevada', 'capital': 'Carson City', 'year_admitted' : 1864} )
print(states)
