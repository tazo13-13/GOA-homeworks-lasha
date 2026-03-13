# 1
integer = [10,20,29,40,50,60,70,]
inte_ger = integer.pop(-1)
integer.append(30)
print(integer)


# 2
surname = input("შეიყვანე გვარი: ")

if "shvili" in surname:
    print(True)
else:
    print(False)


# 3
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
integer = int(input("enter integer 1-5 :"))
numbers.pop(integer)
numbers.insert(0, "change")
print(numbers)


# 4
fruits = ["apple", "banana", "grape", "kiwi", "mango"]
for i in fruits:
    print(i.upper())


# 5
movie = input("enter your favorite movie :")
letter = input("enter your letter :")
if letter in movie :
    print(True)
else:
    print(False)