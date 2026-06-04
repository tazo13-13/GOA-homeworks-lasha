# 0
# tuple-ს და set-ს ორივეს შეუძლია რამდენიმე მნიშვნელობის შენახვა ერთ ცვლადში.


#1
tuple = (10, 20, 30, 40, 50)
T, *U, PLE = tuple
print(T)  
print(U)  
print(PLE)  


# 2
names = {"Lasha", "Giorgi", "Nika", "levani"}

name = input("შეიყვანე სახელი: ")

if name in names:
    print("ეს სახელი არის სეტში და აღარ დაემატება")
else:
    names.add(name)
    print("სახელი დაემატა სეტში")
    print(names)


# 3
tuplee = ("apple","banana","kiwi",)
listt = list(tuplee)
listt.append("მარწყვი")

print(listt)


# 4
# already done classwork!