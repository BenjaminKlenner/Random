group1 = ["Blank","IPhone", "Samsung", "Other Phone"]
group2 = ["Blank","Apple Watch", "Samsung Watch", "Other watch"]
group3 = ["Blank","Airpods", "Samsung Buds", "Other earphones"]

def calculator(module_one,module_two,module_three):
    print("Module 1: {}\nModule 2: {}\nModule 3: {}".format(group1[module_one],group2[module_two],group3[module_three]))
    print("Your unique code is: {}{}{}".format(module_one,module_two,module_three))
    input("Press 'Enter' to restart")
    menu()

def module_definer():
  module_total = int(input("How many modules would you like you're product to have?\nThere is a max of 3 "))
  while module_total > 3 or module_total < 1:
    module_total = int(input("Invalid number, please pick a number between 1 and 3 "))
  module_picker(module_total)


def module_picker(module_total):
  module_one = 0
  module_two = 0
  module_three = 0
  if module_total >= 1:
      module_one = int(input("Please pick 1 module from this list:"))
      if module_total >= 2:
          module_two = int(input("Please pick 1 module from this list:"))
      else:
          calculator(module_one,module_two,module_three)
      if module_total == 3:
          module_three = int(input("Please pick 1 module from this list:"))
          calculator(module_one,module_two,module_three)
      else:
          calculator(module_one,module_two,module_three)
  else:
      module_definer()


def upload():
    code = input("Enter your unqiue code here: ")                
    while int(code[0]) >= 4 or int(code[0]) <= -1:
        code = input("Invalid code, try again:1 ")
    while int(code[1]) >= 4 or int(code[1]) <= -1:
        code = input("Invalid code, try again:2 ")
    while int(code[2]) >= 4 or int(code[2]) <= -1:
        code = input("Invalid code, try again:3 ")
    
    module_one = int(code[0])
    module_two = int(code[1])
    module_three = int(code[2])
    calculator(module_one,module_two,module_three)
    

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
