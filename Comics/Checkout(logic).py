import os

#This document has all the different types of logic needed for the comic book checkout program



#Making lists
Name = []
Stock = []
Price = []
spacer = "-=-"



#Creates lists based off stored data in file
def Start():
    space = 0
    f = open("database.txt", "r")
    i = 1

    while True:
        data = str(f.readline())[:-1]
        i += 1
        if data == "":
            break
        if data[0] == "#":
            continue
        
        if str(data) == str(spacer):
            space += 1
        elif space == 0:
            Name.append(data)
        elif space == 1:
            Stock.append(data)
        elif space == 2:
            Price.append(data)
        elif space == 3:
            break

    f.close()
    Menu()



    
#Menu 
def Menu():
    

    op1 = "1. New Sale\n"
    op2 = "2. Check Stock\n"
    op3 = "3. Check Price\n"
    op4 = "4. \n"
    op5 = "5. \n"
    op6 = "6. Display All\n"
    op7 = "7. Close\n"
    
    option = int(input("What would you like to do?\n{}{}{}{}{}{}{}".format(op1, op2, op3, op4, op5, op6, op7)))

    if option == 1:
        Sale()
    if option == 2:
        CheckStock()
    if option == 3:
        CheckPrice()
    if option == 4:
        Remove()
    if option == 5:
        Edit()
    if option == 6:
        Display()
    if option == 7:
        print("Closing...")


#Sale
def Sale():
    total_price = 0
    total_amount = 0
    receipt = []

    while True:
        item = int(input("What comic book would you like?\n")) - 1
        amount = int(input("How many copies of '{}'?\n".format(Name[item])))

        Stock[item] = (int(Stock[item]) - amount)
        total_price += (float(Price[item]) * float(amount))
        total_amount += amount

        receipt.append(Name[item])
        receipt.append(amount)
        receipt.append((float(Price[item]) * float(amount)))

        print("-----")
        skip = int(input("1. Buy More\n2. Finish\n"))
        if skip == 2:
            break

    i = -1
    ItemNumber = 1
    print("-----\n\n")
    while i + 3 <= len(receipt):
        print("{} | {} | {} | {}".format(ItemNumber,receipt[1 + i],receipt[2 + i],receipt[3 + i]))
        i += 3
        ItemNumber += 1
    print("\n-----=+=-----")
    print("Total items: {}\nTotal cost: {}".format(total_amount,total_price))
    print("\n----------=+=----------")
    skip = input("Press 'Enter' to continue")
    print("\n\n")

    Save()

    
            


#Display:
def Display():
    i = 0
    while i != len(Name):
        print("{} | {} | {} | ${}".format(i + 1,Name[i],Stock[i],Price[i]))
        i += 1
    print("\n----------=+=----------")
    skip = input("Press 'Enter' to continue")
    print("\n\n")
    Menu()


        
#Price Check:
def CheckPrice():
    

    ID = int(input("What comic book would you like?\n")) - 1

    print("Price: ${}".format(Price[ID]))
    print("\n----------=+=----------")
    skip = input("Press 'Enter' to continue")
    print("\n\n")
    Menu()


#Price Check:
def CheckStock():
    

    ID = int(input("What comic book would you like?\n")) - 1

    print("Stock: {}".format(Stock[ID]))
    print("\n----------=+=----------")
    skip = input("Press 'Enter' to continue")
    print("\n\n")
    Menu()





#Saving information
def Save():
    
    if os.path.exists("database.txt"):
        os.remove("database.txt")
    f = open("database.txt", "a")

    i = 0
    f.write("#Name:\n")
    while i != len(Name):
        f.write("{}\n".format(Name[i]))
        i += 1
    f.write(spacer + "\n")
    f.write("#Stock:\n")
    i = 0
    while i != len(Stock):
        f.write("{}\n".format(Stock[i]))
        i += 1
    f.write(spacer + "\n")
    f.write("#Price:\n")
    i = 0
    while i != len(Price):
        f.write("{}\n".format(Price[i]))
        i += 1
    f.close()

    Menu()


Start()
