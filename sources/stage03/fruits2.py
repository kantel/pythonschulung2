fruits2 = ["🍏", "🍅", "🍌", "🍊", "🍋"]
print(fruits2)

for i in range(len(fruits2)):
    if fruits2[i] == "🍌":
        a = i
        # fruits2.pop(i)

fruits2.pop(a)
print(fruits2)

# del(fruits2[fruits2.index("🍏")])
fruits2.remove("🍏")
print(fruits2)