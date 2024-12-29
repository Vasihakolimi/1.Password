import random
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*','(',')']
print("WELCOME TO PASSWORD MANAGER!!")
n1 = int(input("how many letters are you want:"))
n2 = int(input("how many number are you want:"))
n3 = int(input("huw many symbol are you want:"))
password_list = []
for i in range(1,n1+1):
    char =random.choice(letter) 
    password_list+=char
for i in range(1,n2+1):
    char = random.choice(number)
    password_list+=char
for i in range(1,n3+1):
    char = random.choice(symbol)
    password_list+=char
print("password:",password_list)  
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password+=char
print("secure password:",password)