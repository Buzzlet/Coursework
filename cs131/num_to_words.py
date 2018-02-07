# Numbers to words




def print_digit(number):
    """ """
    if(number == 1):
        print("one")
    elif(number == 2):
        print("two")
    elif(number == 3):
        print("three")
    elif(number == 4):
        print("four")
    elif(number == 5):
        print("five")
    elif(number == 6):
        print("six")
    elif(number == 7):
        print("seven")
    elif(number == 8):
        print("eight")
    elif(number == 9):
        print("nine")


def print_teens(number):
    if(number == 10):
        print("ten")
    elif(number == 11):
        print("eleven")
    elif(number == 12):
        print("twelve")
    elif(number == 13):
        print("thirdteen")
    elif(number == 14):
        print("fourteen")
    elif(number == 15):
        print("fifteen")
    elif(number == 16):
        print("sixteen")
    elif(number == 17):
        print("seventeen")
    elif(number == 18):
        print("eightteen")
    elif(number == 19):
        print("nineteen")

def Main():
    user_num = int(input("Enter an integer from -999 to 999: "))
    if(user_num < 0):
        user_num *= -1
        print("negative ", end = '')

    if(user_num > 99):
        print_digit(user_num // 100)
        print("hundred")

    if(user_num % 100 < 20 and user_num % 100 >= 10):
        print_teens(user_num % 100)

    if(user_num < 10):
        print_digit(user_num)

Main()
