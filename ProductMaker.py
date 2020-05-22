group1 = ["IPhone", "Samsung", "Other Phone"]
group2 = ["Apple Watch", "Samsung Watch", "Other watch"]
group3 = ["Airpods", "Samsung Buds", "Other earphones"]

def calculator(module_one,module_two,module_three):
    print(module_one,module_two,module_three)
    


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
      


print("Welcome to the custom product maker")
menu_choice = int(input("1. Start New\n2. Upload design\n"))

if menu_choice == 1:
    print("Starting new design...")
    module_definer()
elif menu_choice == 2:
    print("paste unique product code here: ")



