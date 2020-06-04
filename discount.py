def discount_calculator(price,discount):
    price_after_discount = float("{:.2f}".format(price - (price * (discount/100))))
    print("\n${} after a {}% discount is: \n${}\n\n----------=+=----------\n".format(price,discount,price_after_discount))
    hold = input("Press enter to restart")
    print("\n")
    start()

def start():
    price = float(input("How much does the product cost?\n"))
    discount  = int(input("What is the discount?\n"))
    discount_calculator(price,discount)


start()
