# Koda fragments, kas tiek izpildita vairakkart

'''
def "funkcijas nosaukums"(parametri)
'''

# def square(input_integer: int) -> input_integer:
#     '''
#     Funkcija, kas sklaitli izvada kvadrata
#     '''
#     print("skaitls kvadrata ", pow(input_integer,2))

# square(-4)

# parbauda vai ir pirmskaitlis

def check_prime(x: int):
    if (x==1) or (x==0):
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
        else:
            return True
    
check_prime(55)

# Lokalie un globalie mainigie

def s():
    t,r,c = 1,2,3
    print(t,r,c)
s()

s(r)

# Globalie mainigie
w = 'hello'
y = 100

def q():
    r,t = 2,3
    print(r,t,w)
q()

def q():
    print(w)
    r,t=2,3
    w='tt'
    print(r,t,w)

a = 10
def s():
    global a
    a = 4
    b =22
    print(a,b)
s()
