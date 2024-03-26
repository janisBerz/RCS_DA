### Turpinajums par fnkcijam
# Noklusetas vertibas jaraksta beigas

## Elementu pakosana

a,b = 1,2
a,b = [1,2]
a, b, c = [1,2,True]
a,b,c, = [1,2,3]

# nopakots elements
a,*b,c, d = [1,2,3,4,5]

a,b,c,*d = 'abcdef'

# atlaut patvaliga izmera mainigo virkni
def f(*args):
    for i in args:
        print(i)

# Iepakot atslegas

def f(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

f(a=1,b=2,c=4)

vardnica = {'a1': 900, 'a2': 300, 'a3': 500}
type(vardnica)

vardnica.items()
vardnica.keys()
vardnica.values()

for x in vardnica.items():
    print(x)

for x in vardnica.keys():
    vardnica[x] = x
    
print(vardnica)


d = {'z1': 200, 'z2': 300, 'z4':500}
for x in d.keys():
    d[x]= d[x] -100
print(d)

for k,v in d.items():
    d[k]= v -100

#### Lambda ( anonima funkcija - nav ne 'def', ne 'return)
'''
lambda "arg": "expression"
'''
lambda a,b: print(a,b)
f = lambda a,b: print(a,b)
f(3,5)

### Fiunckcija map
'''
map(funkcija, iterable obj)
'''

my_list = [-1,-2,3,4]
list(map(abs,my_list))

list(map(lambda x: x**2,my_list))

### Filter funkcija
'''
filter(logiska izteiksme, iterejams objekts)
'''

list1 = [1,2,3,4,6,8,9,0]

list(filter(lambda x: x > 4, list))

### Zip funkcija



list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

list(zip(list1,list2,list3))
