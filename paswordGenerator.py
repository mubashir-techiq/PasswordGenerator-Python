import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols=['~','!','@','#','$','%','^','&','*','(',')',':','\"','|','}','{','+','_','?','>','<',',','.','/','/',';','\\','\'',']','[','-','=',']','}']

print('Welcome to Password Generator App')
input('Press Enter to Start')
no = int(input('How many Characters you want?\n'))
nN = int(input('How many Numbers you want?\n'))
nS = int(input('How many Symbols you want?\n'))
pas = []
for i in range(no):
    if nN != 0:
        pas.append(random.choice(numbers))
        nN-=1
    elif nS != 0:
        pas.append(random.choice(symbols))
        nS-=1
    else:
        pas.append(random.choice(letters))

random.shuffle(pas)
my_pas = ''
for i in pas:
    my_pas+=i
print(f'Your Generated Password is : {my_pas}')