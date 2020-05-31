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

    calculator(order,custom_cost,custom_pizzas)

def custom_pizza(pizza_total,custom_cost,order,custom_pizzas):
    custom_pizzas.append(len(custom_pizzas) + 1)
    print(custom_pizzas)
    crust = int(input("What crust do you want?\n1. Thin\n2. Thick\n3. Stuffed"))
    if crust == 1:
        custom_pizzas[len(custom_pizzas) - 1] = "1"
    elif crust == 2:
        custom_pizzas[len(custom_pizzas) - 1] = "2"
    elif crust == 3:
        custom_pizzas[len(custom_pizzas) - 1] = "3"
    else:
        while int(crust) <= 0 and int(crust) >= 3:
            crust = input("What crust do you want?\n1. Thin\n2. Thick\n3. Stuffed")
    main_topping = int(input("What main topping do you want?\n1. Pepperoni\n2. Ham\n3. Cheese\n4. Chicken\n5. Assorted Vegetables"))
    if main_topping == 1:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "1"
    elif main_topping == 2:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "2"
    elif main_topping == 3:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "3"
    elif main_topping == 4:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "4"
    elif main_topping == 5:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "5"
    else:
        while int(main_topping) <= 0 and int(main_topping) >= 5:
            main_topping = int(input("What main topping do you want?\n1. Pepperoni\n2. Ham\n3. Cheese\n4. Chicken\n5. Assorted Vegetables"))
    second_topping = int(input("What secondary topping do you want?\n1. Cheese\n2. Pineapple\n3. Assorted Vegetables\n4. Bacon Bits\n5. None"))
    if second_topping == 1:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "1"
    elif second_topping == 2:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "2"
    elif second_topping == 3:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "3"
    elif second_topping == 4:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "4"
    elif second_topping == 5:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "5"
    else:
        while int(second_topping) <= 0 and int(second_topping) >= 5:
            second_topping = int(input("What secondary topping do you want?\n1. Cheese\n2. Pineapple\n3. Assorted Vegetables\n4. Bacon Bits\n5. None"))
    tertiary_topping = int(input("What tertiary topping do you want?\n1. Cheese\n2. Garlic\n3. Bacon Bits\n4. Basil\n5. None"))
    if tertiary_topping == 1:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "1"
    elif tertiary_topping == 2:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "2"
    elif tertiary_topping == 3:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "3"
    elif tertiary_topping == 4:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "4"
    elif tertiary_topping == 5:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "5"
    else:
        while int(tertiary_topping) <= 0 and int(tertiary_topping) >= 5:
            tertiary_topping = int(input("What tertiary topping do you want?\n1. Cheese\n2. Garlic\n3. Bacon Bits\n4. Basil\n5. None"))
    sauce = int(input("What sauce do you want?\n1. Barbeque\n2. White Garlic\n3. Buffalo\n4. Pesto\n5. None"))
    if sauce == 1:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "1"
    elif sauce == 2:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "2"
    elif sauce == 3:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "3"
    elif sauce == 4:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "4"
    elif sauce == 5:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "5"
    else:
        while int(sauce) <= 0 and int(sauce) >= 5:
            sauce = int(input("What sauce do you want?\n1. Barbeque\n2. White Garlic\n3. Buffalo\n4. Pesto\n5. None"))
            
        
    pizzamaker(pizza_total,custom_cost,order,custom_pizzas)
            
    


def calculator(order,custom_cost,custom_pizzas):
    #Cost Vars
    #Basic Pizza Costs
    p_1 = 6.00
    p_2 = 5.50
    p_3 = 5.00
    #Crust Costs
    c_1 = 1.50
    c_2 = 2.00
    c_3 = 3.50
    #Main Topping Costs
    t1_1 = 2.00
    t1_2 = 2.00
    t1_3 = 1.00
    t1_4 = 2.50
    t1_5 = 1.50
    #Secondary Topping Costs
    t2_1 = 1.00
    t2_2 = 1.50
    t2_3 = 1.50
    t2_4 = 2.00
    t2_5 = 0.00
    #Tertiary Topping Costs
    t3_1 = 1.00
    t3_2 = 1.50
    t3_3 = 2.00
    t3_4 = 1.00
    t3_5 = 0.00
    #Sauce Costs
    s_1 = 1.00
    s_2 = 1.50
    s_3 = 1.50
    s_4 = 2.00
    s_5 = 0

    i = len(custom_pizzas)
    print(custom_pizzas)
    while i > 0:
        #Crust
        if int(custom_pizzas[i - 1][0]) == 1:
            custom_cost += c_1
        elif int(custom_pizzas[i - 1][0]) == 2:
            custom_cost += c_2
        elif int(custom_pizzas[i - 1][0]) == 3:
            custom_cost += c_3
        #Main Topping
        if int(custom_pizzas[i - 1][1]) == 1:
            custom_cost += t1_1
        elif int(custom_pizzas[i - 1][1]) == 2:
            custom_cost += t1_2
        elif int(custom_pizzas[i - 1][1]) == 3:
            custom_cost += t1_3
        elif int(custom_pizzas[i - 1][1]) == 4:
            custom_cost += t1_4
        elif int(custom_pizzas[i - 1][1]) == 5:
            custom_cost += t1_5
        #Secondary topping
        if int(custom_pizzas[i - 1][2]) == 1:
            custom_cost += t2_1
        elif int(custom_pizzas[i - 1][2]) == 2:
            custom_cost += t2_2
        elif int(custom_pizzas[i - 1][2]) == 3:
            custom_cost += t2_3
        elif int(custom_pizzas[i - 1][2]) == 4:
            custom_cost += t2_4
        elif int(custom_pizzas[i - 1][2]) == 5:
            custom_cost += t2_5
        #Tertiary topping
        if int(custom_pizzas[i - 1][3]) == 1:
            custom_cost += t3_1
        elif int(custom_pizzas[i - 1][3]) == 2:
            custom_cost += t3_2
        elif int(custom_pizzas[i - 1][3]) == 3:
            custom_cost += t3_3
        elif int(custom_pizzas[i - 1][3]) == 4:
            custom_cost += t3_4
        elif int(custom_pizzas[i - 1][3]) == 5:
            custom_cost += t3_5
        #Sauce
        if int(custom_pizzas[i - 1][4]) == 1:
            custom_cost += s_1
        elif int(custom_pizzas[i - 1][4]) == 2:
            custom_cost += s_2
        elif int(custom_pizzas[i - 1][4]) == 3:
            custom_cost += s_3
        elif int(custom_pizzas[i - 1][4]) == 4:
            custom_cost += s_4
        elif int(custom_pizzas[i - 1][4]) == 5:
            custom_cost += s_5
        i -= 1
    
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
