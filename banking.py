def storage():
    balances = [0, 0]
    menu(balances)



def menu(balances):
    account_list = ["Spending", "Savings"]
    option = int(input("What account would you like to access?\n1. Spending\n2. Savings\n"))
    if option == 1:
        account = 0
    elif option == 2:
        account = 1
    else:
        while option <= 0 or option >= 2:
            option = int(input("What account would you like to access?\n1. Spending\n2. Savings\n"))

    option = int(input("What would you like to do to {} account?\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Transfer\n".format(account_list[account])))
    if option == 1:
        balance(account_list,account,balances)
    elif option == 2:
        withdraw(account_list,account,balances)
    elif option == 3:
        deposit(account_list,account,balances)
    elif option == 4:
        transfer(account_list,account,balances)
    else:
        while option <= 0 or option >= 4:
            option = int(input("What would you like to do to {} account?\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Transfer\n".format(account_list[account])))
            


def balance(account_list,account,balances):
    print("Balance of {} is: ${}".format(account_list[account],balances[account]))
    menu(balances)
    
    
    
def withdraw(account_list,account,balances):
    print("Withdraw from {}:".format(account_list[account]))
    withdraw = int(input("How much would you like to withdraw?\n1. $5\n2. $10\n3. $20\n4. $50\n5. $100\n6. Custom\n"))
    if withdraw == 1:
        balances[account] -= 5
        print("New balance is: ${}".format(balances[account]))
    elif withdraw == 2:
        balances[account] -= 10
        print("New balance is: ${}".format(balances[account]))
    elif withdraw == 3:
        balances[account] -= 20
        print("New balance is: ${}".format(balances[account]))
    elif withdraw == 4:
        balances[account] -= 50
        print("New balance is: ${}".format(balances[account]))
    elif withdraw == 5:
        balances[account] -= 100
        print("New balance is: ${}".format(balances[account]))
    elif withdraw == 6:
        amount = int(input("How much would you like to withdraw?\n"))
        balances[account] -= amount
        print("New balance is: ${}".format(balances[account]))
    else:
        while withdraw <= 0 or withdraw >= 6:
            withdraw = int(input("How much would you like to withdraw?\n1. $5\n2. $10\n3. $20\n4. $50\n5. $100\n6. Custom\n"))

    menu(balances)
    
    
def deposit(account_list,account,balances):
    print("Deposit to {}:".format(account_list[account]))
    deposit = int(input("How much would you like to deposit?\n1. $5\n2. $10\n3. $20\n4. $50\n5. $100\n6. Custom\n"))
    if deposit == 1:
        balances[account] += 5
        print("New balance is: ${}".format(balances[account]))
    elif deposit == 2:
        balances[account] += 10
        print("New balance is: ${}".format(balances[account]))
    elif deposit == 3:
        balances[account] += 20
        print("New balance is: ${}".format(balances[account]))
    elif deposit == 4:
        balances[account] += 50
        print("New balance is: ${}".format(balances[account]))
    elif deposit == 5:
        balances[account] += 100
        print("New balance is: ${}".format(balances[account]))
    elif deposit == 6:
        amount = int(input("How much would you like to deposit?\n"))
        balances[account] += amount
        print("New balance is: ${}".format(balances[account]))
    else:
        while deposit <= 0 or deposit >= 6:
            deposit = int(input("How much would you like to deposit?\n1. $5\n2. $10\n3. $20\n4. $50\n5. $100\n6. Custom\n"))

    menu(balances)


def transfer(account_list,account,balances):
    print("Which account would you like to transfer to?")
    i = len[account_list]
    a = 0
    while i > 0:
        print("{}. {}\n".format(i,account_list[a]))
        a += 1
        i -= 1

    
    
storage()
