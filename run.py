'''Slot Machine'''
import random

print("-----------------------------------")
print('------------Wellcome To------------')
print("-----------------------------------")
print("-----------SLOT MACHINE------------")
print("-----------------------------------")
print("Starting 1000 money added")
print("One spin cost 10")
print("-----------------------------------")

while True: #main game function
    DESITION = str(input("Type [S] to Spin [E] to Exit :"))
    num1 = random.randint(1,5) #num1, num2, num3 numbers can be changed 0-9 for harder difficulity
    num2 = random.randint(1,5)
    num3 = random.randint(1,5)
    if DESITION == "S":
        print("-----------------------------------")
        print(f"\t\t{num1}|{num2}|{num3}")
        print("-----------------------------------")
        if num1 == num2 == num3:
            print("you won 1000")
        else:
            print("you lost 10")
    elif DESITION == "E":
        print("Thank you for playing. Game closing...")
        break
    else:
        print("wrong input")
print("-----------------------------------")
