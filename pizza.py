def pizzapicker():
    pizza_total = int(input("How many pizzas do you want? "))
    pizzamaker(pizza_total)

def pizzamaker(pizza_total,custom_cost):
    order = []
    while pizza_total != 0:
        pizza = int(input("What pizza flavour do you want?\n1. Pepperoni\n2. Hawaiian\n3. Cheese\n"))
        if pizza == 1:
            order.append(1)
            pizza_total -= 1
        elif pizza == 2:
            order.append(2)
            pizza_total -= 1
        elif pizza == 3:
            order.append(3)
            pizza_total -= 1
        elif pizza == 4:
            order.append(4)
            custom_pizza(order)
            pizza_total -= 1
        else:
            while int(pizza) <= 0 and int(pizza) >= 4:
                pizza = int(input("What pizza flavour do you want?\n1. Pepperoni\n2. Hawaiian\n3. Cheese\n"))

        calculator(order)

def custom_pizza(order):
    print("Make custom pizza")
    custom_cost = 10
    pizzamaker(custom_cost,order)
            
    


def calculator(order,custom_cost):
    #Cost Vars
    p_1 = 6.00
    p_2 = 5.50
    p_3 = 5.00

    
    i = len(order)
    pizza_cost = 0

    while i > 0:
        if int(order[i - 1]) == 1:
            pizza_cost += p_1
        elif int(order[i - 1]) == 2:
            pizza_cost += p_2
        elif int(order[i - 1]) == 3:
            pizza_cost += p_3
        i -= 1

    print(pizza_cost)

pizzapicker()
