# Metodes


a = 'text'
a.upper()
a.capitalize()

t = 'Sodien ir ceturdiena'
t.title()

# Skaitit simbolu skaitu
t.count('i',4,9)
# atrast simbolu (noteikt simbola indeksu, pozicijas numurs)
t.find('i')
t.find('i', 4,9)
t.find('i') >= 0
t.replace('i','D')
t.replace(' ', '',1)

# Parbaudit vai ir skaitls
a = '23432444'
a.isdigit()

a = 'teksts'

type(a)

str_lst = list(a)
str_lst

str(str_lst)
# SareKSTU PARVEIDOT PAR STRING
"".join(str_lst)

b = 'L_eksts'
'L_'+a

str_lst[0] = 'L_'
str_lst
''.join(str_lst)

my_lis = [1,2 ,'teskst', [3,4]]

my_lis[3][1]

4 in my_lis[3]

# skaitit elementus
my_lis.count(2)

# Paplasinat sarakstu
print('Pirms: ', my_lis)
my_lis.append(10)
print('Pec: ', my_lis)

print('Pirms: ', my_lis)
my_lis.extend([11])
print('Pec: ', my_lis)

my_lis.remove(11)

my_lis = [1,2,3,4]
my_lis.clear()
my_lis
del my_lis


my_lis = [1,2,5,8,9,4]
my_lis.sort()
my_lis

# Ka dabut min/mx vertibas

min(my_lis)
max(my_lis)

len(my_lis)
my_lis[-1]
my_lis[len(my_lis)-1]