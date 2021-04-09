# Make sure you have a clear readable Menu

print('''
--------------------------
Welcome to ABC Electronics
--------------------------
1. View Items
2. Buy Items
3. Exit
''')

# Make sure the choices are numerical and in order when customer is inputing their choice

choice = int(input("Enter Your Option = "))

if choice == 1:
    print("*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Items Available in ABC Electronics")
    # Make sure the data is opened in read mode and that the proper txt file is linked
    data = open("inventory.txt", "r")
    items = data.readlines()
    # Make the inventory list readable and user friendly
    print("*-*-*-*-*-*-*-*-*-*-*-*-*")
    for item in items:
        name, price, count = item.split(",")
        print("{0}\t{1}\t{2}".format(name, price, count))
    print("*-*-*-*-*-*-*-*-*-*-*-*-*")

if choice == 2:
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Please Select the Item you want")
    # Make sure the data is opened in read mode and that the proper txt file is linked
    data = open("inventory.txt", "r")
    items = data.readlines()
    # Make the inventory list readable and user friendly
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    for item in items:
        name, price, count = item.split(",")
        print("{0}\t{1}\t{2}".format(name, price, count))
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")