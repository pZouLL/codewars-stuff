number = int(input("Number : "))


import math

pi = math.pi
final = ""

def check():
    pi = math.pi
    final = ""
    for x in range(0,number + 1) :
        pi = str(pi)
        pi1 = pi[x]
        final = final + pi1
    return final

def check2():
    pi = math.pi
    final = ""
    for x in range(0,number + 1) :
        pi = str(pi)
        pi1 = pi[x]
        final = final + pi1
    return x

final1 = check()
index = check2()
pi = str(pi)
lastindex = pi[index]
final1 = final1 + lastindex 

print(final1)