import random

pick = "1234567890"


Length = 10
final = ""
for i in range(0,Length):
    satum = random.choice(pick)
    final = final + satum
print("Number : " , final)
    