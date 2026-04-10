# 1
# while loop - მუშაობს სანამ პირობა სწორი არ იქნება.
# for loop - მუშაობს მაშინ როცა წინასწარ ვიცით რამდენჯერ უნდა გამოიტანოს კოდი.


# 2
rdr = "lesson"

for i in rdr:
    print(i)


# 3

i = 2

while i <= 25:
    print(i)
    i += 3


# 4
list = ["lasha","giorgi","saba","vano","aleqsi","tazo"]

string = input("შეიყვანე სტრინგიი: ")

list.insert(4,string)

print(list)


# 5
numbers = [13, 12, 97, 24, 243, 30]

numbers.remove(24)

print(numbers)


# 6
list = ["lasha","giorgi","saba","vano","aleqsi","tazo"]
string = input("enter randomm string: ")


list.pop(3)

print(list)