def menu():
    type = int(input('Press "1" for Numeric - Binary\nPress "2" for Binary - Numeric\n'))
    if type == 1:
        number = int(input("Enter a number between 0 - 255\n"))
        while number < 0 or number > 255:
            number = int(input("Enter a number between 0 - 255\n"))
        num_bin(number)
    elif type == 2:
        binary = input("Enter a binary number\nA binary number is a 8 digit number that is either 1 or 0\n")
        while len(binary) != 8:
            binary = input("Enter a binary number\nA binary number is a 8 digit number that is either 1 or 0\n")
        bin_num(binary)

def bin_num(binary):
    result = 0
    
    if binary[0] != "0":
        result += 128
    elif (binary[0]) != "1":
        result = result
    else:
        print("Invalid number: {}".format(binary[0]))
        
    if (binary[1]) != "0":
        result += 64
    elif (binary[1]) != "1":
        result = result
    else:
        print("Invalid number: {}".format(binary[1]))
        
    if (binary[2]) != "0":
        result += 32
    elif (binary[2]) != "1":
        result = result
    else:
        print("Invalid number: {}".format(binary[2]))
        
    if (binary[3]) != "0":
        result += 16
    elif (binary[3]) != "1":
        result = result
    else:
        print("Invalid number: {}".format(binary[3]))
        
    if (binary[4]) != "0":
        result += 8
    elif (binary[4]) != "1":
        result = result
    else:
        print("Invalid number: {}".format(binary[4]))
        
    if (binary[5]) != "0":
        result += 4
    elif (binary[5]) != "1":
        result = result
    else:
        print("Invalid number: {}".format(binary[5]))
        
    if (binary[6]) != "0":
        result += 2
    elif (binary[6]) != "1":
        result = result
    else:
        print("Invalid number: {}".format(binary[6]))

    if (binary[7]) != "0":
        result += 1
    elif (binary[7]) != "1":
        result = result
    else:
        print("Invalid number: {}".format(binary[7]))

    print(result)
    input("Press 'Enter' to restart")
    menu()

      
def num_bin(number):
    value_128 = 1
    value_64 = 1
    value_32 = 1
    value_16 = 1
    value_8 = 1
    value_4 = 1
    value_2 = 1
    value_1 = 1

    if number / 128 < 1 or number / 128 > 2:
        value_128 = 0
    else:
        number -= 128

    if number / 64 < 1 or number / 128 > 2:
        value_64 = 0
    else:
        number -= 64

    if number / 32 < 1 or number / 128 > 2:
        value_32 = 0
    else:
        number -= 32

    if number / 16 < 1 or number / 128 > 2:
        value_16 = 0
    else:
        number -= 16

    if number / 8 < 1 or number / 128 > 2:
        value_8 = 0
    else:
        number -= 8

    if number / 4 < 1 or number / 128 > 2:
        value_4 = 0
    else:
        number -= 4

    if number / 2 < 1 or number / 128 > 2:
        value_2 = 0
    else:
        number -= 2

    if number / 1 < 1 or number / 128 > 2:
        value_1 = 0
    else:
        number -= 1


    print(value_128,value_64,value_32,value_16,value_8,value_4,value_2,value_1)
    input("Press 'Enter' to restart")
    menu()
    




menu()
        
    
        
