# 2
age1 = (True and False)
age2 = (True and True)
age3 = (False and False)
age4 = (False and True)

age1 = (True or False)
age2 = (True or True)
age3 = (False or False)
age4 = (False or True)


# 3
name1 = str(input("enter your name: "))
name2 = int(input("enter your age: "))
name3 = float(input("enter your heigh: "))
if name1 == "lasha" and name2 >= 18 and name3 == 1.80:
    print("same")
else:
    print("not same")


# 4
num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))
result1 = (num1 % num2)
print("ნაშთია" , result1)


# 5
age = int(input("enter your age : "))
if age % 2 == 0 :
    print("რიცხვი არის ლუწი")
else :
    print("რიცხვი არის კენტი")