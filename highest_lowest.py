

# find highest and lowest number from space seperated numbers
def highest(n) :
    highest = 0
    for x in n :
        if x > highest :
            highest = x 
    return(highest)

def lowest(n) :
    lowest1 = n[0]
    for i in n : 
        if i < lowest1:
            lowest1 = i
    return(lowest1)

heist = input("Enter a range of numbers seperated with a space : ")
heist1 = list(map(int ,heist.split(' ')))
print(heist1)
high = highest(heist1)
low = lowest(heist1)

print(high , " " , low )