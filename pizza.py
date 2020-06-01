def pizzapicker():
    pizza_total = 0
    custom_cost = []
    pizza_order = []
    drink_order = []
    custom_pizzas = []
    a = 1
    pizza_total = int(input("How many pizzas do you want?\n"))
    i = pizza_total
    pizzamaker(pizza_total,custom_cost,pizza_order,custom_pizzas,a,i,drink_order)


def pizzamaker(pizza_total,custom_cost,pizza_order,custom_pizzas,a,i,drink_order):
    while i > 0:
        pizza = int(input("Pizza {}/{} flavour:\n1. Pepperoni\n2. Hawaiian\n3. Cheese\n4. Custom\n".format(a,pizza_total)))
        if pizza == 1:
            pizza_order.append(1)
            i -= 1
            a += 1
        elif pizza == 2:
            pizza_order.append(2)
            i -= 1
            a += 1
        elif pizza == 3:
            pizza_order.append(3)
            i -= 1
            a += 1
        elif pizza == 4:
            i -= 1
            a += 1
            custom_pizza(pizza_total,custom_cost,pizza_order,custom_pizzas,a,i,drink_order)
        else:
            while int(pizza) <= 0 and int(pizza) >= 4:
                pizza = int(input("Pizza {}/{} flavour:\n1. Pepperoni\n2. Hawaiian\n3. Cheese\n4. Custom\n".format(a,pizza_total)))
                
    sidespicker(pizza_order,custom_cost,custom_pizzas,drink_order)

def custom_pizza(pizza_total,custom_cost,pizza_order,custom_pizzas,a,i,drink_order):
    custom_pizzas.append(len(custom_pizzas) + 1)
    
    #Crust picker
    crust = int(input("What crust do you want?\n1. Thin\n2. Thick\n3. Stuffed\n"))
    if crust == 1:
        custom_pizzas[len(custom_pizzas) - 1] = "1"
    elif crust == 2:
        custom_pizzas[len(custom_pizzas) - 1] = "2"
    elif crust == 3:
        custom_pizzas[len(custom_pizzas) - 1] = "3"
    else:
        while int(crust) <= 0 and int(crust) >= 3:
            crust = input("What crust do you want?\n1. Thin\n2. Thick\n3. Stuffed\n")
    #Main Topping picker
    main_topping = int(input("What main topping do you want?\n1. Pepperoni\n2. Ham\n3. Cheese\n4. Chicken\n5. Assorted Vegetables\n"))
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
    #Secondary Topping picker
    secondary_topping = int(input("What secondary topping do you want?\n1. Cheese\n2. Pineapple\n3. Assorted Vegetables\n4. Bacon Bits\n5. None\n"))
    if secondary_topping == 1:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "1"
    elif secondary_topping == 2:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "2"
    elif secondary_topping == 3:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "3"
    elif secondary_topping == 4:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "4"
    elif secondary_topping == 5:
        custom_pizzas[len(custom_pizzas) - 1] = custom_pizzas[len(custom_pizzas) - 1] + "5"
    else:
        while int(secondary_topping) <= 0 and int(secondary_topping) >= 5:
            secondary_topping = int(input("What secondary topping do you want?\n1. Cheese\n2. Pineapple\n3. Assorted Vegetables\n4. Bacon Bits\n5. None\n"))
    #Tertiary Topping picker
    tertiary_topping = int(input("What tertiary topping do you want?\n1. Cheese\n2. Garlic\n3. Bacon Bits\n4. Basil\n5. None\n"))
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
            tertiary_topping = int(input("What tertiary topping do you want?\n1. Cheese\n2. Garlic\n3. Bacon Bits\n4. Basil\n5. None\n"))
    #Sauce picker
    sauce = int(input("What sauce do you want?\n1. Barbeque\n2. White Garlic\n3. Buffalo\n4. Pesto\n5. None\n"))
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
            sauce = int(input("What sauce do you want?\n1. Barbeque\n2. White Garlic\n3. Buffalo\n4. Pesto\n5. None\n"))
            
        
    pizzamaker(pizza_total,custom_cost,pizza_order,custom_pizzas,a,i,drink_order)

def sidespicker(pizza_order,custom_cost,custom_pizzas,drink_order):     
    drink_total = int(input("How many drinks do you want?\n"))
    i = drink_total
    a = 0
    while i > 0:
        drink = int(input("Drink {}/{}:\n1. 1.5L Coke\n2. 1.5L Fanta\n3. 1.5L Lift\n4. 500ml Coke\n5. 500ml Fanta\n6. 500ml Lift\n".format(a,drink_total)))
        if drink == 1:
            drink_order.append(1)
            i -= 1
            a += 1
        elif drink == 2:
            drink_order.append(2)
            i -= 1
            a += 1
        elif drink == 3:
            drink_order.append(3)
            i -= 1
            a += 1
        elif drink == 4:
            drink_order.append(4)
            i -= 1
            a += 1
        elif drink == 5:
            drink_order.append(5)
            i -= 1
            a += 1
        elif drink == 6:
            drink_order.append(6)
            i -= 1
            a += 1
        else:
            while int(drink) <= 0 and int(drink) >= 6:
                drink = int(input("Drink {}/{}:\n1. 1.5L Coke\n2. 1.5L Fanta\n3. 1.5L Lift\n4. 500ml Coke\n5. 500ml Fanta\n6. 500ml Lift\n".format(a,drink_total)))
    
    calculator(pizza_order,custom_cost,custom_pizzas,drink_order)


def calculator(pizza_order,custom_cost,custom_pizzas,drink_order):
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
    #Drink Costs
    d1_5l = 3.00
    d500ml = 2.00

    
    i = len(custom_pizzas)
    custom_pizza_receipt = []
    while i > 0:
        custom_cost.append(len(custom_cost) + 1)
        custom_pizza_receipt.append(len(custom_pizza_receipt) + 1)
        #Crust Calc
        if int(custom_pizzas[i - 1][0]) == 1:
            custom_cost[len(custom_cost) - 1] = c_1
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = "Thin "
        elif int(custom_pizzas[i - 1][0]) == 2:
            custom_cost[len(custom_cost) - 1] = c_2
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = "Thick "
        elif int(custom_pizzas[i - 1][0]) == 3:
            custom_cost[len(custom_cost) - 1] = c_3
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = "Stuffed "
        #Main Topping Calc
        if int(custom_pizzas[i - 1][1]) == 1:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t1_1
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Pepperoni "
        elif int(custom_pizzas[i - 1][1]) == 2:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t1_2
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Ham "
        elif int(custom_pizzas[i - 1][1]) == 3:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t1_3
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Cheese "
        elif int(custom_pizzas[i - 1][1]) == 4:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t1_4
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Chicken "
        elif int(custom_pizzas[i - 1][1]) == 5:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t1_5
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Assorted Vegetables "
        #Secondary topping Calc
        if int(custom_pizzas[i - 1][2]) == 1:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t2_1
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Cheese "
        elif int(custom_pizzas[i - 1][2]) == 2:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t2_2
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Pineapple "
        elif int(custom_pizzas[i - 1][2]) == 3:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t2_3
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Assorted Vegetables "
        elif int(custom_pizzas[i - 1][2]) == 4:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t2_4
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Bacon "
        elif int(custom_pizzas[i - 1][2]) == 5:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t2_5
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| None "
        #Tertiary topping Calc
        if int(custom_pizzas[i - 1][3]) == 1:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t3_1
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Cheese "
        elif int(custom_pizzas[i - 1][3]) == 2:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t3_2
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Garlic "
        elif int(custom_pizzas[i - 1][3]) == 3:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t3_3
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Bacon "
        elif int(custom_pizzas[i - 1][3]) == 4:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t3_4
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Basil "
        elif int(custom_pizzas[i - 1][3]) == 5:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + t3_5
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| None "
        #Sauce Calc
        if int(custom_pizzas[i - 1][4]) == 1:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + s_1
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Barbeque "
        elif int(custom_pizzas[i - 1][4]) == 2:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + s_2
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| White Garlic "
        elif int(custom_pizzas[i - 1][4]) == 3:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + s_3
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Buffalo "
        elif int(custom_pizzas[i - 1][4]) == 4:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + s_4
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| Pesto "
        elif int(custom_pizzas[i - 1][4]) == 5:
            custom_cost[len(custom_cost) - 1] = custom_cost[len(custom_cost) - 1] + s_5
            custom_pizza_receipt[len(custom_pizza_receipt) - 1] = custom_pizza_receipt[len(custom_pizza_receipt) - 1] + "| None "
        i -= 1
    
    i = len(custom_cost)
    a = 0
        
    drink_cost = 0
    drink_receipt = []
    i = len(drink_order)
    while i > 0:
        drink_receipt.append(len(drink_receipt) + 1)
        if int(drink_order[i - 1]) == 1:
            drink_cost += d1_5l
            drink_receipt[len(drink_receipt) - 1] = "1.5L Coke - $" + str(d1_5l)
        elif int(drink_order[i - 1]) == 2:
            drink_cost += d1_5l
            drink_receipt[len(drink_receipt) - 1] = "1.5L Fanta - $" + str(d1_5l)
        elif int(drink_order[i - 1]) == 3:
            drink_cost += d1_5l
            drink_receipt[len(drink_receipt) - 1] = "1.5L Lift - $" + str(d1_5l)
        elif int(drink_order[i - 1]) == 4:
            drink_cost += d500ml
            drink_receipt[len(drink_receipt) - 1] = "500ml Coke - $" + str(d500ml)
        elif int(drink_order[i - 1]) == 5:
            drink_cost += d500ml
            drink_receipt[len(drink_receipt) - 1] = "500ml Fanta - $" + str(d500ml)
        elif int(drink_order[i - 1]) == 6:
            drink_cost += d500ml
            drink_receipt[len(drink_receipt) - 1] = "500ml Lift - $" + str(d500ml)
        i -= 1

    
    pizza_receipt = []
    i = len(pizza_order)
    pizza_cost = 0
    while i > 0:
        pizza_receipt.append(len(pizza_receipt) + 1)
        if int(pizza_order[i - 1]) == 1:
            pizza_cost += p_1
            pizza_receipt[len(pizza_receipt) - 1] = "Pepperoni - $" + str(p_1)
        elif int(pizza_order[i - 1]) == 2:
            pizza_cost += p_2
            pizza_receipt[len(pizza_receipt) - 1] = "Hawaiian - $" + str(p_2)
        elif int(pizza_order[i - 1]) == 3:
            pizza_cost += p_3
            pizza_receipt[len(pizza_receipt) - 1] = "Cheese - $" + str(p_3)
        i -= 1


    #Custom Pizza receipt   
    i = len(custom_pizza_receipt)
    print("\n")
    if i > 0:
        a = 0
        print("Custom Pizzas:\n")
        while a < i:
            print("{} - ${}".format(custom_pizza_receipt[0 + a],custom_cost[0 + a]))
            a += 1
            if a < i:
                print("-")
        print("--\nTotal cost for custom pizzas : ${}".format(sum(custom_cost)))
        print("---\n")

    #Normal Pizza receipt
    i = len(pizza_order)
    if i > 0:
        a = 0
        print("Normal Pizzas:\n")
        while a < i:
            print("{}".format(pizza_receipt[0 + a]))
            a += 1
        print("--\nTotal cost for normal pizzas : ${}".format(pizza_cost))
        print("---\n")
    
    #Drink receipt
    i = len(drink_order)
    if i > 0:
        a = 0
        print("Drinks:\n")
        while a < i:
            print("{}".format(drink_receipt[0 + a]))
            a += 1
        print("--\nTotal cost for drinks : ${}".format(drink_cost))
        print("---\n")

    
    total_cost = sum(custom_cost) + pizza_cost + drink_cost
    print("Total Cost: ${}\n".format(total_cost))
    print("----------=+=----------")
    hold = input("Press enter to restart")
    pizzapicker()
    
pizzapicker()
