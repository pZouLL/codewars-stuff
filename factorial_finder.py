'''
def check_number(n) :
    list1 = []
    if n > 1 : 
        n69 = n 
        for x in range(1 , n) :
            n1 = n69 % x
            if n1 == 0 :
                list1.append(x)
        list1.append(n)
        return list1
    else:
        return "Number Should Be Bigger Than 1"
'''

def check_number(n):
    if n <= 1 : return "Number Should Be Bigger Than 1"
    li = [x for x in range(1,n) if n % x == 0]
    return li

n = int(input("Number : "))
print(check_number(n*2))