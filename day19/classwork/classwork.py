# 1
#  slicing - არის მეთოდი რომლის დახმარებიტაც შეგვილლია ამოვჭრათ რაიმე ტექსტიდან მონაკვეთი.


# 2
numbers = [5, 12, 11, 29, 28, 7, 1]

print(numbers[-3:])


# 3
name = input("შემოიტანე შენი სახელი: ")
print(name[1:4])


# 4
surname = "ტერტერაშვილი"
user_surname = input("შეიყვანე შენი გვარი: ")
if user_surname[:5] == surname[:5]:
    print("almost same")
else:
    print("bye")


# 5
list = [11,22,33,44,55,66,77,]
list[2] = "random"
print(list[:4])


# 6
names = ["nika", "vano", "giorgi", "luka", "aleqsandre"]
start = int(input("Enter start: "))
stop = int(input("Enter stop: "))

if start < stop and start >= 0 and start <= 4 and stop >= 1 and stop <= 5:
    print(names[start: stop])
else:
    print("Incorrect Index!")


# 7
names = ["nika", "vano", "giorgi", "luka", "aleqsandre"]
start = int(input("Enter start: "))
stop = int(input("Enter stop: "))

if start < stop and start >= 0 and start <= 4 and stop >= 1 and stop <= 5:
    print(names[start: stop])
else:
    print("სწორია Index!")