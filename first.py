from functools import reduce
people = [
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Fred Ward", "age": 77},
    {"name": "finn Carter", "age": 59},
    {"name": "Ariana Richards", "age": 40},
    {"name": "Victor Wong", "age": 74},
]
#print(people)
sorted_by_name = sorted(people, key=lambda l:l['name'].lower())
print(sorted_by_name)
name_dec = list(map(lambda l: f" {l['name']} is {l['age']} years old", sorted_by_name))
print(name_dec)

under_seventy = sorted(filter(lambda l:l['age'] < 70, sorted_by_name), key = lambda l:l['age'])
print(under_seventy)
under_seven = map(lambda l:l['age'],under_seventy)
red = reduce(lambda acc, l: acc + l, under_seven, 0)
print(red)