#Dictionaries, Oh Lovely Dictionaries
#Dictionary data structure in Python
#A Dictionary (or ”dict”) is a way to store data just like a list

#a list lets you do this:

things = ['a', 'b', 'c', 'd']

print(things[1])

things[1] = 'z'

print(things[1])

print(things)

#You can use numbers to ”index” into a list
#you can only use numbers to get items out of a list.

#What a dict does is let you use anything, not just numbers.
#Yes, a dict associates one thing to another, no matter what it is. Take a look:

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}

print(stuff['name'])

print(stuff['age'])

print(stuff['height'])

stuff['city'] = "SF"

print(stuff['city'])

stuff['name'] = "litsoe"

stuff['fruit'] = 'banana'

print(stuff)



print(len(stuff))

stuff[1] = 3

stuff[2] = "Neato"

print(stuff[1])

print(stuff[2])

print(stuff)

del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)
{'name': 'Zed', 'age': 39, 'height': 74}

#”mapping” or ”associating” is the key concept in a dictionary.
# create a mapping of state to abbreviation
states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}


# create a basic set of states and some cities in them
cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}


# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
#states contained in state is state.items()
#list(state.items())

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
