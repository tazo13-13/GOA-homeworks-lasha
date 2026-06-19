# 0
# .remove ს გადაეცემა ტექსტი რომლის წაშლაწ გვინდა set-იდან, არასწორი სტრინგის გადაცემის შემთხვევაში ერორია
#.update გამოიყენება ერთი სეტის მნიშვნელობის გასანახლებლად.
# .add გამოიყენება set ში ელემენტის ჩასამატებლად
# .pop სეტიდან შლის რანდომულ ელემენტს.
# .clear გამოიყენება ყველაფრის წაშლაში სეტიდან.
# .discard ს გადაეცემა ელემენტი რომლის წაშლაც გვინდა სეტიდან . არასწორი სტრინგის გადაცემისას არ გვიერორებს.
# . intersection ორი სეტიდა ნ ვიღებთ ერთნაირ ანუ საერთო ელემენტს.
# .difference გამოიყენება set ების  შორის განსხვავების საპოვნელად.
# .symmetric_difference გვიბრუნებს იმ ელემენტს რომლებიც არიან ერთ ერთ სეტში.


# 1
# discard() ასევე შლის მითითებულ ელემენტს სეტიდან,  მაგრამ თუ ელემენტი სეტში არ არსებობს, შეცდომას არ გამოიტანს.
# discard ასევე შლის მითითებულ ელემენტს სეტიდან, მაგრამ თუ ელემენტი სეტში არ არსებობს, ერორს არ გამოიტანს.


# 2
names = {"soso", "lasha", "saba", "avto"}
names.discard("soso")
print(names)


# 3
cars = {"BMW", "Mercedes", "Toyota", "Audi"}
cars2 = {"Audi", "Toyota", "BUGATI", "Ford"}
print(cars.intersection(cars2))


# 4
cars_1 = {"BMW", "Mercedes", "Toyota", "Audi"}
cars_2 = {"Audi", "Toyota", "Honda", "Ford"} 

CARSS= cars_1.union(cars_2)

print(CARSS)


# 5
drinks = ["cola", "sprite", "fanta", "red fanta - my favorite!!!!!"]

drinks.remove("sprite")

print(drinks)


# 6
set__1 = {112, 22, 3, 40, 53}
set__2 = {30, 53, 6, 7, 8}

print(set__1.difference(set__2))
print(set__2.difference(set__1))


# 7
print(set__1.symmetric_difference(set__2))


# 8
surnames = {"terterashvili", "keshelava", "boyoveli", "motiashvili"}

surnames.clear()

print(surnames)