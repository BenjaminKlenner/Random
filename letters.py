



def counter(letter):
    sentence = input('What sentence would you like to check for: "{}"\n'.format(letter))
    count = sentence.count(letter)
    print(count)
    hold = input("----------=+=----------\nPress enter to restart\n")
    start()


def start():
    letter = input("What letter would you like to count\n")
    if len(letter) == 1:
        counter(letter)
    else:
        print("Invalid letter\nYou entered '{}'".format(letter))
        while len(letter) != 1:
            letter = input("What letter would you like to count\n")
        counter(letter)

start()
