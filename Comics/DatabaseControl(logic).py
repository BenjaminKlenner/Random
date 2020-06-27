import os

#This document has all the different types of logic needed for the comic book database control program



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
    

    op1 = "1. Display database\n"
    op2 = "2. Add new comic\n"
    op3 = "3. Pull specific data\n"
    op4 = "4. Remove specific data\n"
    op5 = "5. Edit specific data\n"
    op6 = "6. Check Stock\n"
    op7 = "7. Add Stock\n"
    op8 = "8. Close\n"
    
    option = int(input("What would you like to do?\n{}{}{}{}{}{}{}{}".format(op1, op2, op3, op4, op5, op6, op7, op8)))

    if option == 1:
        Display()
    if option == 2:
        Push()
    if option == 3:
        Pull()
    if option == 4:
        Remove()
    if option == 5:
        Edit()
    if option == 6:
        CheckStock()
    if option == 7:
        AddStock()
    if option == 8:
        print("Closing...")


#Check Stock:
def AddStock():
    ID = int(input("What entry would you like to add stock too?\n")) - 1
    NewStock = int(input("New Stock for {}:\nCurrent: {}\n".format(Name[ID],Stock[ID])))
    Stock[ID] = int(Stock[ID]) + NewStock
    print("Restocked {}\nNew Stock: {}".format(Name[ID], Stock[ID]))
    print("\n----------=+=----------")
    skip = input("Press 'Enter' to continue")
    print("\n\n")
    Save()



#Check Stock:
def CheckStock():
    LowStock = []
    i = 0
    
    StockBelow = int(input("Stock below or equal too __?\n"))
    
    while i < len(Stock):
        if int(Stock[i]) <= StockBelow:
            LowStock.append(Name[i])
            LowStock.append(Stock[i])
            i += 1
        else:
            i += 1
            continue
    if len(LowStock) == 0:
        print("All stock is good")
    else:
        print("{} items have low stock\n-----\nItems:\n".format(int(len(LowStock)/2)))
        i = 0
        while i < len(LowStock):
            print("{} | {}".format(LowStock[i],LowStock[i + 1]))
            i += 2
        print("\n----------=+=----------")
        skip = input("Press 'Enter' to continue")
        print("\n\n")

    Menu()
            




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
    

        
#Getting data:
def Pull():
    

    ID = int(input("What entry would you like?\n")) - 1

    print("Name: {}\nStock: {}\nPrice: ${}".format(Name[ID], Stock[ID], Price[ID]))
    print("\n----------=+=----------")
    skip = input("Press 'Enter' to continue")
    print("\n\n")
    Menu()


#Remove data:
def Remove():
    ID = int(input("What entry would you like to remove?\n")) - 1
    delete = int(input("Are you sure you want to remove:\nName: {} | Stock: {} | Price: ${}\n1. Yes\n2. No\n".format(Name[ID], Stock[ID], Price[ID])))

    if delete == 1:
        Name.pop(ID)
        Stock.pop(ID)
        Price.pop(ID)
        print("\n----------=+=----------")
        skip = input("Press 'Enter' to continue")
        print("\n\n")
        Save()
    elif delete == 2:
        print("\n\n")
        Menu()


#Edit data:
def Edit():
    ID = int(input("What entry would you like to edit?\n")) - 1

    NewName = input("New Name:\nCurrent: {}\nPress 'Enter' to keep original name\n".format(Name[ID]))
    NewStock = input("New Stock:\nCurrent: {}\nPress 'Enter' to keep original stock\n".format(Stock[ID]))
    NewPrice = input("New Price:\nCurrent: {}\nPress 'Enter' to keep original price\n".format(Price[ID]))


    if str(NewName) != "":
        Name[ID] = NewName
    if str(NewStock) != "":
        Stock[ID] = NewStock
    if str(NewPrice) != "":
        Price[ID] = NewPrice
    print("New data:\nName: {} | Stock: {} | Price: ${}".format(Name[ID], Stock[ID], Price[ID]))
    print("\n----------=+=----------")
    skip = input("Press 'Enter' to continue")
    print("\n\n")
    Save()


    

#Adding new data
def Push():
    NewName = str(input("What is the name of the new comic book?\n"))
    NewStock = int(input("How much stock of {} do you have?\n".format(NewName)))
    NewPrice = float(input("How much will {} cost?\n".format(NewName)))

    Name.append(NewName)
    Stock.append(NewStock)
    Price.append(NewPrice)

    print("Reference number for {} is: {}".format(NewName,len(Name)))
    print("\n----------=+=----------")
    skip = input("Press 'Enter' to continue")
    print("\n\n")
    Save()


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
