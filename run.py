'''Slot Machine'''
import random
import os

ACCOUNT = 100  # starting money + update after effect
WINS = 0  # counting wins

print("-----------------------------------")
print("      Welcome to slot machine      ")
print("      100 added to account...      ")
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


while True:  # main game function
    print("  [s] to Spin   |   [e] to Exit")
    DESITION = str(input("-----------------------------------\n   Type :"))
    num1 = random.randint(1, 5)  # (1, 5)  >>> (0, 9) for harder difficulity
    num2 = random.randint(1, 5)  # change all nums
    num3 = random.randint(1, 5)  # to get harder difficulty
    if DESITION == "s":  # start game
        os.system('clear')  # ('cls') windows, ('clear') linux/mac
        print("-----------------------------------")
        print("-----------------------------------")
        print("----------| SLOT MACHINE |---------")
        print("-----------------------------------")
        print("-----------|   |   |   |-----------")
        print(f"-----------| {num1} | {num2} | {num3} |-----------")
        print("-----------|   |   |   |-----------")
        print("-----------------------------------")
        print("-----------------------------------")
        if num1 == num2 == num3:
            ACCOUNT += 1000  # addition to account (on win)
            WINS += 1  # addition to win
            print("-----------------------------------")
            print(f"   MONEY : {ACCOUNT}     JACKPOTS : {WINS}")
            print("-----------------------------------")
            print("           You won 1000            ")
            print("-----------------------------------")
        elif ACCOUNT <= 0:
            print("Out of money. Game closing...")
            print("-----------------------------------")
            break
        else:
            ACCOUNT -= 10  # subtract from account (on lose)
            print("-----------------------------------")
            print(f"   MONEY : {ACCOUNT}     JACKPOTS : {WINS}")
            print("-----------------------------------")
            print("           You lost 10             ")
            print("-----------------------------------")
    elif DESITION == "e":  # exit the game
        print("-----------------------------------")
        print("Thanks for playing. Game closing...")
        print("-----------------------------------")
        break
    else:
        os.system('clear')  # ('cls') windows, ('clear') linux/mac
        print("-----------------------------------")
        print("           Wrong input             ")
        print("-----------------------------------")
