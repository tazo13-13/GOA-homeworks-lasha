# 1
# სია არის მონაცემთა სტრუქტურა, რომელიც ინახავს რამდენიმე მნიშვნელობას ერთ ცვლადში.


# 2
list = [5, 10, 15, 20, 25]
print(list[2])


# 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 3 == 0:
        print("divisible by 3")


# 4
random = "python!"
print(random[-3:])


# 5
names = ["lasha", "saba", "Giorgi", "vano", "dato", "lazare"]
user_name = input("შეიყვანეთ თქვენი სახელი: ")
count = 0

for name in names:
    if name == user_name:
        print("user name")
        count += 1
print(count)


# 6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
for num in numbers:
    if num % 2 == 0:      
        even_sum+= num  
print(even_sum)


# 7
names = ["Giorgi", "Ana", "Gvantsa", "Nino", "Goga", "Luka"]
for name in names:
    if name.lower().startswith("g"):  
        print(name, True)