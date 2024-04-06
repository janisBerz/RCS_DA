# range(2)
# list(range(2))

# list(range(4,10))

# list(range(0,7,2))

# list(range(10,1,-1))

# v = iter(range(3))
# v

# iter(v)

# next(v)


# t = iter('text')

# next(t)

# # Cikli (while)

# '''
# while nosacijums (True vai False):
#     izpildas kods, jan nosacijums ir speka
# else: # si dala nav obligata
#     izpildas kods, ja nosacijums nav speka
# '''

# x =10
# while x>0:
#     x-= 1
#     print(x)


# my_list = []
# i = 0
# while len(my_list)<4:
#     my_list.append(i)
#     i+=2
#     print(my_list)
    
    
# # Skaitit saraksta elementu summa
# my_list = [23,45,12,10,25]
# i = 0
# summa = 0
# while i<len(my_list):
#     summa = summa + my_list[i]
#     i+=1
#     print(summa)

# # Alternativa

# it_list = iter(my_list)
# summa = 0
# while i<len(my_list):
#     summa += next(it_list)
#     i+=1
#     print(summa)
    
# Izprintet nepara skaitlus no 0..10

int_list = list(range(11))
n = 0
while n<=10:
    if int_list[n]%2 !=0:
        print(f'{n}')
        n += 1

n = 0
while n<=6:
    n+=1
    if n == 3:
        pass # izlaiz un nedara neko
    print('papildus', n)


# For Loop

el_list = [2,4,6,7,1,8]

for el in el_list:
    if el % 2 ==0:
        print(el)


int_list = [23,25,12,27]
it_list = iter(int_list)
summa = 0
#Iegut elementu summu

for _ in range(len(int_list)):
    summa += next(it_list)
    print(summa)
    
# saraksts, izprintet elementus kvadrata

list1 = [3,5,7,8]
new_list = []
for int in list1:
    new_list.append(pow(int, 2))

print(new_list)

# cikls ciklaa

word_list = ["mekney", "like", "banana"]

for word in word_list:
    print(word)
    for letter in word:
        print(letter.capitalize())


# List comprehension
'''
[isteiksme(vai) for val in saraksts]
'''

a = [1,2,3,4,5,6,7,8]
abs(a)


[abs(x) for x in a]
[x**2 for x in a]


a = input()
a

type(a)

a.split()

[int(x) for x in a.split()]

# dubults cikls

[(i,j) for i in 'abc' for j in range(3)]

[i+j for i in range(5) for j in range(7)]

# Izmantot nosacijumu, pielietot if konstrukciju

my_list = [1,2,3,4,5,6,7,8]

# izprintet para skaitli
[x for x in my_list if x%2 ==0]

l = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,4,5]
# iegut unikalo skaitli 

new_l = []
for el in l:
    if el not in new_l:
        new_l.append(el)
print(new_l)

l = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,4,5]
l_unique = []
[l_unique.append(el) for el in l if not el not in l] 