# 1
name = input("enter your name:")
if name == "lasha" :
    print("HELLO!")
else :
    print("Bye")


# 2
my = (30)
your = int(input("enter your favorite number: "))
if my == your:
    print("Perfect")
elif your > my :
    print("More")
else:
    print("less")


# 3
age = int(input("enter your age:"))
name = input("enter your name:")
my_age = 14
my_name = "lasha"
if age == my_age and name ==my_name:
    print("twins")
else:
    print("not twins")


# 4
number = int(input("შეიყვანე რიცხვი: "))

if number % 3 == 0 and number % 5 == 0:
    print("number is 3-ისა and 5-ის ჯერადი")
else:
    print("number is not 3-ისა and 5-ის ჯერადი")


# 5
password = input("შეიყვანე პაროლი: ")

if len(password) < 8:
    print("სუსტი პაროლი")
else:
    print("კარგი პაროლი")