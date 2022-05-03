import random
import sys


def flipcoin():
    head_or_tail = ["head" , "tail"]
    decider = random.choice(head_or_tail)
    print(decider)


loop = 69
while loop == 69 :
    flipcoin1 = input("Flip Coin? (Y/N) : ")
    if flipcoin1.lower() == "y" :
        flipcoin()
    if flipcoin1.lower() == "n" :
        sure = input("You Want To Exit? (Y/N) : ")
        if sure.lower() == "y" :
            loop = 420
            sys.exit(1)
        if sure.lower() == "n" :
            pass