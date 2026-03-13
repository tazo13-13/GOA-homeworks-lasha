# 1
#  .upper() - ამის მეშვეობით წინადადება დიდი ასოებით იწერება.
#  .lower() - ამის მეშვეობით წინადადება იწერება პატარა ასოებით.
#  .capitalize() - ამის მეშვეობით წინადადების პირველი ასო იწერება დიდი ასოთი დანარჩენი პატარა ასოთი.


# 2
name = input("enter your name: ")
print(name.upper())


# 3
names = ["lasha", "nika", "giorgi", "dato", "ana"]
for name in names:
    print(name.capitalize())


# 4
surname = input("enter your surnam: ")
if "t" in surname:
    print(True)
else:
    print(False)


# 5
surname = input("bro enter your surname : ")
case = input(" wich case upper / lower / capitalize / none :")

if case == "upper":
    print(surname.upper())

elif case == "lower":
    print(surname.lower())

elif case == "capitalize":
    print(surname.capitalize())

else:
    print("არასწორია")


# 6
sentence = input("შეიყვანე წინადადება: ")
symbol = input("შეიყვანე სიმბოლო: ")
print(sentence.find(symbol))


# 7
sentence = input("შეიყვანე წინადადება: ")
symbol = input("შეიყვანე სიმბოლო: ")

for i in range(len(sentence)):
    if sentence[i] == symbol:
        print(i)






# 1
names = ["ლაშა", "გიორგი", "ნიკა", "მარიამ"]
if "გიორგი" in names:
    names.remove("გიორგი")
print(names)


# 2
fruits = ["ვაშლი", "ბანანი", "გრეიფრუტი", "ანანასი"]
last_item = fruits.pop()  
print( fruits)
print( last_item)


# 3
names = ["ლაშა", "ნიკა", "მარიამ", "თამარი"]
names.insert(2,"ალექსანდრე")
print(names)


# 4
names = ["ლაშა", "ნიკა", "მარიამ"]
new_name = input("გთხოვთ, შეიყვანოთ თქვენი სახელი: ")
names.append(new_name)
print(names)


# 5
numbers = [10, 20, 30, 40, 50]

favorite_number = int(input("შეიყვანეთ თქვენი საყვარელი რიცხვი: "))
index_input = int(input("შეიყვანეთ ინდექსი: "))

if 0 <= index_input < len(numbers):
    numbers.insert(index_input, favorite_number)
    print("რიცხვი " + str(favorite_number) + " ჩასმულია ინდექსზე " + str(index_input) + ".")
else:
    print(" ინდექსი სიაში არ არსებობს.")

print("განახლებული სია: " + str(numbers))


# 7
names = ["ლაშა", "ნიკა", "მარიამ", "თამარ"]
index_input = int(input("შეიყვანეთ ინდექსი (0-3): "))
if 0 <= index_input < len(names):
    removed_item = names.pop(index_input)  
    print(f"ელემენტი '{removed_item}' ამოღებულია.")
else:
    print("არასწორიa!")

print(names)