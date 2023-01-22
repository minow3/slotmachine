'''Slot Machine'''
import random

print("-----------------------------------")
print('------------Wellcome To------------')
print("-----------------------------------")
print("-----------SLOT MACHINE------------")
print("-----------------------------------")
print("Starting 1000 money added...")
print("-----------------------------------")
print("     SPIN 10     |     WIN 1000    ")
print("-----------------------------------")

while True: #main game function
    DESITION = str(input(" Type [S] Spin   |   [E] to Exit :"))
    num1 = random.randint(1,5) #(1,5)  >>> (0,9) for harder difficulity
    num2 = random.randint(1,5)
    num3 = random.randint(1,5)
    if DESITION == "S": # start game
        print("-----------------------------------")
        print(f"\t\t{num1}|{num2}|{num3}") # align to center
        print("-----------------------------------")
        if num1 == num2 == num3:
            print("you won 1000")
        else:
            print("you lost 10")
    elif DESITION == "E": # exit the game
        print("Thanks for playing. Game closing...")
        break
    else:
        print("wrong input")
print("-----------------------------------")
