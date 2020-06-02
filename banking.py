#Lots of bugs with bad data catch and transfer doesn't work sometimes (can't deposit into account and then use transfer function)

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
        #doesn't work
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
        #doesn't work
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
        #doesn't work
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
        #doesn't work
        while deposit <= 0 or deposit >= 6:
            deposit = int(input("How much would you like to deposit?\n1. $5\n2. $10\n3. $20\n4. $50\n5. $100\n6. Custom\n"))

    menu(balances)


def transfer(account_list,account,balances):


    
    print("Which account would you like to transfer to?")
    a = 0
    i = len(account_list)
    while i > 0:
        if a != account:
            print("{}. {}".format(a + 1,account_list[a]))
        a += 1
        i -= 1
    i = len(account_list)
    option = int(input(""))
    while i > 0:
        #doesn't work
        if option <= 0 or option >= len(account_list):
            print("Which account would you like to transfer to?")
            b = 0
            c = len(account_list)
            while c > 0:
                if b != account:
                    print("{}. {}".format(b + 1,account_list[b]))
                b += 1
                c -= 1
            option = int(input(""))
        
        elif option - 1 == account:
            print("Which account would you like to transfer to?")
            b = 0
            c = len(account_list)
            while c > 0:
                if b != account:
                    print("{}. {}".format(b + 1,account_list[b]))
                b += 1
                c -= 1
            option = int(input(""))
            
        elif option - 1 != account:
            transfer_account = option - 1
        i -= 1
        a += 1
    



    print(transfer_account)
    transfer = int(input("How much would you like to transfer?\n1. $5\n2. $10\n3. $20\n4. $50\n5. $100\n6. Custom\n"))
    if transfer == 1:
        balances[account] -= 5
        balances[transfer_account] += 5
        print("New balance for {} is: ${}".format(account_list[account],balances[account]))
        print("New balance for {} is: ${}".format(account_list[transfer_account],balances[transfer_account]))
    elif transfer == 2:
        balances[account] -= 10
        balances[transfer_account] += 10
        print("New balance for {} is: ${}".format(account_list[account],balances[account]))
        print("New balance for {} is: ${}".format(account_list[transfer_account],balances[transfer_account]))
    elif transfer == 3:
        balances[account] -= 20
        balances[transfer_account] += 20
        print("New balance for {} is: ${}".format(account_list[account],balances[account]))
        print("New balance for {} is: ${}".format(account_list[transfer_account],balances[transfer_account]))
    elif transfer == 4:
        balances[account] -= 50
        balances[transfer_account] += 50
        print("New balance for {} is: ${}".format(account_list[account],balances[account]))
        print("New balance for {} is: ${}".format(account_list[transfer_account],balances[transfer_account]))
    elif transfer == 5:
        balances[account] -= 100
        balances[transfer_account] += 100
        print("New balance for {} is: ${}".format(account_list[account],balances[account]))
        print("New balance for {} is: ${}".format(account_list[transfer_account],balances[transfer_account]))
    elif transfer == 6:
        amount = int(input("How much would you like to transfer?\n"))
        balances[account] -= amount
        balances[transfer_account] += amount
        print("New balance for {} is: ${}".format(account_list[account],balances[account]))
        print("New balance for {} is: ${}".format(account_list[transfer_account],balances[transfer_account]))
    else:
        #doesn't work
        while transfer <= 0 or transfer >= 6:
            transfer = int(input("How much would you like to transfer?\n1. $5\n2. $10\n3. $20\n4. $50\n5. $100\n6. Custom\n"))
    menu(balances)
    
    
storage()
