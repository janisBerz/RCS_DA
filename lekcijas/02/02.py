# Int
a = 5
b = -5

print(a)

# Float
a = 1.5
print(type(a))

# Convert to float
float(b)
print(type(b))

# List (saraksts)
l1 = [1,2,3,4]
l2 = [1,"teksts", 2.0]

type(l1)
type(l1[1])
type(l2[2])

#Set (kopa)
s = {1,2,3,4}
s[2]

# Order unique elements
l = [0,3,3,3,3,7,9,2]
sl = set(l)
type(sl)

# Data type: tulep (kortežs)
t = (1,2,3,4)
t
type(t)
t[2]

p_tuple = (0,1,2,3,4,5,6,7,8,9,10)
p_list = [0,1,2,3,4,5,6,7,8,9,10]
print(type(p_tuple), type(p_list))

print(p_tuple.__sizeof__(),
      p_list.__sizeof__()
      )

# Boolean
t = True
f = False

type(t)

# Logiska izteiksme
t = (2+1) == 3
t
(2+3) == 4
# ==, !=, >,<

bool("text")
bool("")
bool(2323)
bool(None)

## Pamatdarbibas ar operatoriem
# Operatori +,-,*, power (kapinasana), %

### Saskaitisana

b = 2+3
b

a = 5
a+= 3
a

# Dalit un reizinat

a = 2
b = 3
a+b

# Parsta dalisana
9/2
9//2

-9//2

## Kapinasa
2**3

pow(2,3)

#mod operacija (noder pie partitates parbaudes)

11%2
6%2
7%2 == 0

## Simbolu virknes
teksts1 = 'abs'
teksst2 = "abs"

teksts_list = list(teksts1)
teksts_list

teksts1[1]
teksts1[0:2]
teksts1[:3]
teksts1[-1]
teksts1[::-1]
teksts1*4
teksts1 + teksst2
teksts1 + '_' + teksst2

# Operacijas ar kopaam

set1 = {1,2,3}
set2 = {4,5,9,3}

# Apvienot 
set1|set2

#Kopigo elementu atrasana
set1 & set2
#starpiba
set1 - set2

# simetriska starpiba (visi, kas nav kopigie)

set1^set2
