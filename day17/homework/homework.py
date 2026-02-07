# 1
numbers = [5, 12, 19, 22, 2, 9, 15]

for num in numbers:
    if num > 10:
        print(num)


# 2
list = [10, "Hello", 3.14, True,5,6]
for i in list:
    print(type(i))


# 3
age = [10,11,12,13,14,15,16,17,18,19]
sum = 0
for i in age:
    sum += i
print(sum)


# 4
names = ["lasha","saba","giorgi"]
num = 0
for i in names:
    print(i, num)
    num += 1


# 5
names = ["lasha","saba","giorgi"]
num = 0
for i in names:
    print(i, num)
    num += 2


# 6
numbers = [1,3,0,-6,-3,2,14,67,0,12,34,64,21]
possitive = 0
negative = 0

for i in numbers:
    if i > 0:
        possitive += i
    elif i < 0:
        negative += 1
else:
    print("zero")