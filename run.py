'''Slot Machine'''
import random
import os

print("-----------------------------------")
print("      Wellcome to slot machine     ")
print("      1000 added to account...     ")
print("-----------------------------------")
print("-----------------------------------")
print("----------| SLOT MACHINE |---------")
print("-----------------------------------")
print("-----------|   |   |   |-----------")
print("-----------| 7 | 7 | 7 |-----------")
print("-----------|   |   |   |-----------")
print("-----------------------------------")
print("-----------------------------------")
print("     SPIN 10     |     WIN 1000    ")
print("-----------------------------------")
print("           LUCKY NUMBERS           ")
print("    111   222   333   444   555    ")
print("-----------------------------------")


while True: #main game function
    print("  [S] to Spin   |   [E] to Exit")
    DESITION = str(input("-----------------------------------\n   Type :"))
    num1 = random.randint(1,5) #(1,5)  >>> (0,9) for harder difficulity
    num2 = random.randint(1,5)
    num3 = random.randint(1,5)
    if DESITION == "S": # start game
        os.system('cls') # ('cls') windows, ('clear') linux/mac
        print("-----------------------------------")
        print("----------| SLOT MACHINE |---------")
        print("-----------------------------------")
        print("-----------|   |   |   |-----------")
        print(f"-----------| {num1} | {num2} | {num3} |-----------")
        print("-----------|   |   |   |-----------")
        print("-----------------------------------")
        print("-----------------------------------")
        if num1 == num2 == num3:
            print("           You won 1000            ")
            print("-----------------------------------")
        else:
            print("           You lost 10             ")
            print("-----------------------------------")
    elif DESITION == "E": # exit the game
        print("-----------------------------------")
        print("Thanks for playing. Game closing...")
        print("-----------------------------------")
        break
    else:
        os.system('cls')
        print("-----------------------------------")
        print("           Wrong input             ")
        print("-----------------------------------")
