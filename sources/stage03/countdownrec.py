def countdown(n):
    if n <= 0:
        print("Whammm … 💥💥💥!!")
    else:
        print(n)
        countdown(n-1)

countdown(10)