import os

#This document has all the different types of logic needed for the comic book program

#Outline:
#I will use lists to store all the different types of comic books, how many of them there are and how much they cost



#Making lists
Name = []
Stock = []
Price = []
spacer = ("-=-")

def Start():
    space = 0
    f = open("database.txt", "r")
    i = 1

    while True:
        data = str(f.readline())
        
        i += 1
        if data == "":
            break
        
        if data == spacer:
            space += 1



    print(space)                
    print(Name)
    Menu()



    
#Menu 
def Menu():
    option = int(input("What would you like to do?\n1. Display database\n2. Add new comic\n3. Pull specific data\n4. Save and close\n"))

    if option == 1:
        Display()
    if option == 2:
        Push()
    if option == 3:
        Pull()
    if option == 4:
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
    

        
#Getting data:
def Pull():
    

    ID = int(input("What entry would you like\n")) - 1

    print("Name: {}\nStock: {}\nPrice: ${}".format(Name[ID], Stock[ID], Price[ID]))
    print("\n----------=+=----------")
    skip = input("Press 'Enter' to continue")
    print("\n\n")
    Menu()





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
    Menu()


#Saving information
def Save():
    
    if os.path.exists("database.txt"):
        os.remove("database.txt")
    f = open("database.txt", "a")

    i = 0
    while i != len(Name):
        f.write("{}\n".format(Name[i]))
        i += 1
    f.write(spacer + "\n")
    i = 0
    while i != len(Stock):
        f.write("{}\n".format(Stock[i]))
        i += 1
    f.write(spacer + "\n")
    i = 0
    while i != len(Price):
        f.write("{}\n".format(Price[i]))
        i += 1
    f.write(spacer)
    f.close()



Start()












