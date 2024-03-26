## Sazarojumi
# bool (boolean) datu tips -> True(1)/False(0)

int(True)
int(False)

bool(0)
bool(1)

bool(10)

bool(None)


## Logical operators, logiskie operatori
# OR
1 or 0
1|0

# AND
1 and 0

True or False
True and False

True and True

# XOR
1^0
1^1

# NOT

not(0)
not(1)
not(True)
not(False)

# Boolean izteiksmes
x = 5
y = 6
x > y

teksts = 'yoyoyoyoy'
'yo' in teksts

int('yo' in teksts)
x<y and 'yo' in teksts
x<y and not('yo' in teksts)

## If, else statements
'''
if (nosacijums)):
    # izpildās, ja nosacījums ir patiess
    print('Izpildās, ja nosacījums ir patiess')
else:
    # izpildās, ja nosacījums nav patiess
    print('Izpildās, ja nosacījums nav patiess')
'''

teksts1 = 'Hello1'
teksts2 = 'Hello2'

# ==, !=, >, <, >=, <=
if (teksts1 == teksts1):
    print('Teksti ir vienādi')
else:
    print('Teksti nav vienādi')

## Salidzinat teksta garumus
teksts1 = 'Hello1'
teksts2 = 'Hello2'

if (len(teksts1) == len(teksts2)):
    print('Teksti ir vienādi')
else:
    print('Teksti nav vienādi')


# Vairaki nosacijumi

teksts = 'Sodien ir otrdiena, saulaina diena'

if 'pirmdiena' in teksts:
    print('Pirma diena')
elif 'otrdiena' in teksts:
    print('otra diena')
elif 'tresdiena' in teksts:
    print('tresdiena')
else:
    print('Nav vairs dienu')
    
    
list1 = [1,3,4,5]
if 5 in list: print('ir ir ir')


list1 = [1,2,3,4,5]
x= 10

if len(list1) > 3:
    x=+1
else:
    x=1

print(x)

x+=1 if len(list1) >3 else print(x)


nedela = ['Pirm','Otrd','Tresd','Ceturtd','Piektd','Sestd','Svētd']
brivdienas = ['Sestd','Svētd']

diena = 'Sestd'

# parbaudi vai dina ir brivdiena

if diena in nedela:
    if diena in brivdienas:
        print('Diena ir brivdiena')
    else:
        print('Diena nav brivdiena')
else:
    print('Nav nedelas diena')

# Alternativs pieraksts

if (diena in nedela) & (diena in brivdienas):
    print('Diean ir brivdiena')
elif (diena in nedela) & (diena in brivdienas):
    print('Diena nav brivdiena')
else:
    print('nav nedelas diena')
    
# Noteikt paritati


x = 4
if x % 2:
    print(f'{x} ir nepara')
else:
    print(f'{x} ir para')