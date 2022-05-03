import random
while True:
    Roll = input("Roll Dice?(Y/N) : ")
    if Roll.lower() == "n" : break
    Dice_amnt = int(input("Input 1 or 2 Dice : "))
    if Roll.lower() == "y" and Dice_amnt == 1 : print(random.randint(1,6))
    if Roll.lower() == "y" and Dice_amnt == 2: print("The 2 Dices Are: " , random.randint(1,6), "and" , random.randint(1,6))