def pizzapicker():
    pizza_total = 0
    order = []
    custom_pizzas = []
    pizza_total = int(input("How many pizzas do you want? "))
    custom_cost = 0
    pizzamaker(pizza_total,custom_cost,order,custom_pizzas)

def pizzamaker(pizza_total,custom_cost,order,custom_pizzas):
    while pizza_total > 0:
        pizza = int(input("What pizza flavour do you want?\n1. Pepperoni\n2. Hawaiian\n3. Cheese\n4. Custom\n"))
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
            pizza_total -= 1
            custom_pizza(pizza_total,custom_cost,order,custom_pizzas)
        else:
            while int(pizza) <= 0 and int(pizza) >= 4:
                pizza = int(input("What pizza flavour do you want?\n1. Pepperoni\n2. Hawaiian\n3. Cheese\n"))

    calculator(order,custom_cost)

def custom_pizza(pizza_total,custom_cost,order,custom_pizzas):
    custom_pizzas.append(len(custom_pizzas) + 1)
    print(custom_pizzas)
    crust = input("What crust do you want?\n1. Thin\n2. Thick\n3. Stuffed")
    if crust == 1:
        custom_pizzas[len(custom_pizzas)] = 1
    elif crust == 2:
        custom_pizzas[len(custom_pizzas)] = 2
    elif crust == 3:
        custom_pizzas[len(custom_pizzas)] = 3
    else:
        while int(crust) <= 0 and int(crust) >= 3:
            crust = input("What crust do you want?\n1. Thin\n2. Thick\n3. Stuffed")

        
    custom_cost += 10
    pizzamaker(pizza_total,custom_cost,order,custom_pizzas)
            
    


def calculator(order,custom_cost):
    #Cost Vars
    p_1 = 6.00
    p_2 = 5.50
    p_3 = 5.00

    
    i = len(order)
    pizza_cost = custom_cost

    while i > 0:
        if int(order[i - 1]) == 1:
            pizza_cost += p_1
        elif int(order[i - 1]) == 2:
            pizza_cost += p_2
        elif int(order[i - 1]) == 3:
            pizza_cost += p_3
        i -= 1

    print("{}".format(pizza_cost))
    hold = input("Press enter to restart")
    pizzapicker()
    
pizzapicker()
