group1 = ["Blank","IPhone X", "Galaxy S10", "Other Phone"]
group2 = ["Blank","Apple Watch", "Samsung Watch", "Other watch"]
group3 = ["Blank","Airpods", "Samsung Buds", "Other earphones"]


def calculator(module_one,module_two,module_three,engrave):
#module prices
#example: g10 | g = group | 1 = group number | 0 = item number
    total_price = 20
    g10 = 0
    g11 = 25
    g12 = 20
    g13 = 20
    g20 = 0
    g21 = 10
    g22 = 15
    g23 = 10
    g30 = 0
    g31 = 8
    g32 = 5
    g33 = 5

#calculates module prices
    if module_one == 0:
        total_price += g10
    elif module_one == 1:
        total_price += g11
    elif module_one == 2:
        total_price += g12
    elif module_one == 3:
        total_price += g13
        
    if module_two == 0:
        total_price += g20
    elif module_two == 1:
        total_price += g21
    elif module_two == 2:
        total_price += g22
    elif module_two == 3:
        total_price += g23
        
    if module_three == 0:
        total_price += g30
    elif module_three == 1:
        total_price += g31
    elif module_three == 2:
        total_price += g32
    elif module_three  == 3:
        total_price += g33

#calculates engraving cost
    if engrave == "0":
        engrave_message = "No engraving"
    else:
        engrave_message = engrave
        engrave_cost = len(engrave) * 0.20
        total_price += engrave_cost

#displays costs
        
    print("Module 1: {}\nModule 2: {}\nModule 3: {}\nEngraved text: {}".format(group1[module_one],group2[module_two],group3[module_three],engrave_message))
    print("Your design will cost: ${}".format(total_price))
    print("Your unique code is: {}{}{}{}".format(module_one,module_two,module_three,engrave))
    input("Press 'Enter' to restart")
    menu()

#Pick what the product has
def module_definer():
  module_total = int(input("How many modules would you like you're product to have?\nThere is a max of 3 "))
  while module_total > 3 or module_total < 1:
    module_total = int(input("Invalid number, please pick a number between 1 and 3 "))
  engraving = int(input("Would you like an engraving on your product?\n1. Yes\n2. No\n"))
  if engraving == 1:
      engraver(module_total)
  elif engraving == 2:
      engrave = "0"
      module_picker(module_total,engrave)
  #else:

#Pick engrave text
def engraver(module_total):
    engrave = input("What text would you like to engrave?\nEach letter is $0.20\n")
    module_picker(module_total,engrave)


#Pick what the modules are      
def module_picker(module_total,engrave):
  module_one = 0
  module_two = 0
  module_three = 0
  if module_total >= 1:
      module_one = int(input("Please pick 1 module from this list:\n1. IPhone X\n2. Galaxy S10\n3. Other Phone\n"))
      if module_total >= 2:
          module_two = int(input("Please pick 1 module from this list:\n1. Apple Watch\n2. Samsung Watch\n3. Other Watch\n"))
      else:
          calculator(module_one,module_two,module_three,engrave)
      if module_total == 3:
          module_three = int(input("Please pick 1 module from this list:\n1. Airpods\n2. Samsung Buds\n3. Other earphones\n"))
          calculator(module_one,module_two,module_three,engrave)
      else:
          calculator(module_one,module_two,module_three,engrave)
  else:
      module_definer()

#upload exisiting design
def upload():
#validate unique code
    code = input("Enter your unqiue code here: ")                
    while int(code[0]) >= 4 or int(code[0]) <= -1:
        code = input("Invalid code, try again: ")
    while int(code[1]) >= 4 or int(code[1]) <= -1:
        code = input("Invalid code, try again: ")
    while int(code[2]) >= 4 or int(code[2]) <= -1:
        code = input("Invalid code, try again: ")

#turn unique code into correct format
    module_one = int(code[0])
    module_two = int(code[1])
    module_three = int(code[2])
    engrave = code[3:]
    calculator(module_one,module_two,module_three,engrave)
    
#main menu
def menu():
    print("Welcome to the custom product maker")
    menu_choice = input("1. Start New\n2. Upload design\n")

    while int(menu_choice) != 1 and int(menu_choice) != 2:
        print("Invalid option")
        menu_choice = input("1. Start New\n2. Upload design\n")
        
    if int(menu_choice) == 1:
        module_definer()
    elif int(menu_choice) == 2:
        upload()



menu()
