# Dictionary

agents = {
    'name': 'john',
    'surname': 'doe',
    'age': 30,
    'age': 30
}

type(agents)
agents['name']
agents['country'] = 'LV'
agents['secondaryCountries'] = ['GB', 'LT']
agents.keys()
agents.items()


## Alternativs piemers

agents = dict(
    name = 'john',
    surname = 'doe',
    age = 30
)

agents = [['name', 'john'], ['surname', 'doe'], ['age', 30]]
dict(agents)
print(agents)

## var veidot tuksu 
agents = dict()

# veidot vardnicu znot atslegas
agents = dict.fromkeys(['name', 'surname', 'age'])
agents = dict.fromkeys(['name', 'surname', 'age'], 'unknown')
print(agents)