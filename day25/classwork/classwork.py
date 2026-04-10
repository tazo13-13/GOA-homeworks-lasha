# 1
#  ფუნქცია - არის კოდი რომელიც კონკრეტულ დავალებას ასრულებს.


# 2
def sum_of_3(a, b, c):
    return a + b + c

result = sum_of_3(2, 1, 3)
print(result)


# 3
def list(abrr):
    return len(abrr)

numbers = [1, 2, 3, 4, 5]
print(list(numbers))


# 4
def average(numbers):
    return sum(numbers) / len(numbers)
list = [2, 4, 6, 8]
print(average(list))


# 5
list = ["lasha", "saba", "gio", "vano", "dato"]

def insert_string(s, index):
    list.insert(index, s)
    return list

string2 = input(" string: ")
index2 = int(input("enter index: "))

print(insert_string(string2,index2))


# 6
def len(iterable):
    count = 0
    for i in iterable:
        count += 1
    return count

list1 = [10, 20, 30, 40]
string1 = "hello"

print(len(list1))    
print(len(string1))  


# 7
def sum1(numbers):
    count1 = 0
    for num in numbers:
        count1 += num
    return count1

list4 = [5, 10, 25]
print(sum1(list4))  