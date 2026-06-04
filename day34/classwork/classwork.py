# 0
# list - ცვლადია და შეგვიძლია შევცვალოთ ან წავშალოთ ან დავამატოთ.
# tuple - უცვლელია და ვერ შევცვლით.


# 1
sports = ("football", "basketball", "judo", "rugby", "voleyball")


# 2
fruits = ("cucumber", "tomato", "banana", "apple")

(green, red, *yellow) = fruits  

print(green)
print(red)
print(yellow)

# 3
sportslist = list(sports)
sportslist[2] = "swimming"
sports = tuple(sportslist)


# 4
numbers = (4, 9, 12)

num = int(input("enter your number!: "))

print(numbers * num)