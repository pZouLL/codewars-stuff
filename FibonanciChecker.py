import math
import sys
import time
loop=1
while loop == 1 :

    num = int(input("Input (Input '99999' to exit) : "))

    if num == 99999 :
        print("Exiting , Sayonara!")
        time.sleep(1)
        print("Succesfull ")
        sys.exit()


    checker = 5*num**2 + 4
    print(checker)

    checker1 = 5*num**2 - 4
    print(checker1)

    square = math.sqrt(checker)   
    print(square)

    square1 = math.sqrt(checker1)
    print(square1)

    square_string = str(square)
    square1_string = str(square1)
    last_char = square_string[-1]
    last_char2 = square1_string[-1]
    print(last_char)
    print(last_char2)


    if last_char == "0" or last_char2 == "0" :
        print("It is a fibonancii number")

    else:
        print("its not lmao")