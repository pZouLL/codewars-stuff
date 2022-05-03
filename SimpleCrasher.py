import sys
li2 = [1 , 2  , 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
tos = """
(1). Im Not Responsible For Any Damage
(2). Once The Program Runs Your RAM Will Be Filled And Your PC Will Freeze
(3). You Will Have To Cut The Electricity From The PC Once It Freezes
"""
print(tos)
sure = input("Are You Sure? (This Will Break Your PC)(Y/N) : ")
if sure.lower() == 'y' :
    print("Say Bye Bye!")
    loop = 1
    add = 0 
    while loop == 1 :
        for q in li2 :
            add += q
            li2.append(add)

else:
    print("Good Choice")
    sys.exit(1)
                
     