list1 = []
def check_prime(n) :
    for x in range(1,n):
        n1 = n % x
        if n1 == 0 :
            list1.append(x)
    list1.append(n)
    return list1

n = int(input("Enter Number : "))
list2 = check_prime(n)

bool2 = None
t = 0 
for x in list2 :
    t += 1 
    if t == 2 :
        bool2 = True
    else:
        bool2 = False
    
if bool2 == True :
    print("It is Prime")
elif bool2  == False :
    print("IT Is Not Prime")