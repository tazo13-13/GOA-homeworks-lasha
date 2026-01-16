# 1
#Conditional statements - python ში გამოიყენება იმისთვის რომ კოდი შესრულდეს პირობის მიხედვით true or false.


# 2
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age > 18:
    print("adult")
elif 13 <= age <= 18:
    print("teen")
else:
    print("child")


# 3
name = "giorgi"
age = 20

if name == "giorgi":
    if age > 18:
        print("adult giorgi")
    else:
        print("not adult giorgi")
else:
    print("not giorgi")


# 4
age = int(input("enter your age:"))
height = int(input("enter your height:"))
if age%height == 0:
    print(True)
else:
    print(False)


# 5
name = input("enter your best name: ")
favorite_movie = input("enter your favorite movie: ")

if name == "avto":
    print("you are avto")
elif name == "levani" and favorite_movie == "ტიტანიკი":
    print("Levani loves titanic")
else:
    print("someone likes other film")