# 1
for i in range(1, 51, 2):
    print(i)


# 2
username = input("Enter your username :")
for i in username:  
    print(i)


# 3
for i in range(150):
    if  i % 2 == 0:
        print("even")
    else:
        print("odd")


# 4
for i in range(20, -1 , -1) :
    print(i)


# 5
correct_password_is = "1234"
password = input("Enter your password: ")

while password != correct_password_is:
    print("password is not true")
    password = input("enter your password again")

print("pasword corect")