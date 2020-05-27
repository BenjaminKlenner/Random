def pizzapicker():
    pizza_total = int(input("How many pizzas do you want?"))
    pizzamaker(pizza_total)

def pizzamaker(pizza_total):
    order = []
    while pizza_total != 0:
        pizza = int(input("What pizza flavour do you want?\n1. Pepperoni\n2. Hawaiian\n3. Cheese"))
        if pizza == 1:
            order.append(1)
            print("pepperoni")
            pizza_total -= 1
        elif pizza == 2:
            order.append(2)
            print("Hawaiian")
            pizza_total -= 1
        elif pizza == 3:
            order.append(3)
            print("Cheese")
            pizza_total -= 1
        else:
            while int(pizza) <= 0 and int(pizza) >= 3:
                pizza = int(input("What pizza flavour do you want?\n1. Pepperoni\n2. Hawaiian\n3. Cheese"))
            
    print(order)


pizzapicker()
