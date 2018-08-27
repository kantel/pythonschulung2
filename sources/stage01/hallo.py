my_supernumber = 333

def add_number(_my_supernumber):
    my_supernumber = _my_supernumber
    print(my_supernumber)
    my_supernumber += my_supernumber
    print("The number of the beast = " + str(my_supernumber))

print(my_supernumber)
add_number(my_supernumber)
print(my_supernumber)