states = {"oregnon" : "OR","Florida" : "FL","california" : "CA","New york" : "NY","Michigan":"MI"}
cities = {"CA":"San francisco","MI":"Detroit","FL":"Jacksonvile"}

cities["NY"] = "New york"
cities["OR"] = "Portland"

print('-' * 10)
print("NY state has: ",cities['NY'])
print("OR state has: ",cities['OR'])

print('-' * 10)
print("Michigans abbrevation is: ",states['Michigan'])
print("Florida abbrevation is: ",states['Florida'])

print('-' * 10)
print("Michigans abbrevation is: ",cities[states['Michigan']])
print("Florida abbrevation is: ",cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city{cities[abbrev]}")

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no texas.")

city = cities.get('TX','Does not exist')
print(f"The city for state 'TX' is: {city}")