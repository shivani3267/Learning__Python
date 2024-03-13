#Password Generator in Python
import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
        'O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','8','9']
symbols=['!','@','$','%','&','*','(',')','+']
print("Welcome to the Password Generator!")

n_letters=int(input("How many letters you want in your Password?\n"))
n_numbers=int(input("How many numbers you want in your Password?\n"))
n_symbols=int(input("How many symbols you want in your Password?\n"))

password_list=[]

#letter selection for password
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list+=char

#symbol selection for password
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list+=char

#number selection for password
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list+=char

#shuffle password_list
random.shuffle(password_list)
password=""
for i in password_list:
    password+=i

print("Your Password is: ",password)
print("Thank You!\nhave a nice day!")
