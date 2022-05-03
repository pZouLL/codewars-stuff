import sys
numbers = [5,5,5,5,5,5,5,7,5,5,5,5,5,5]

for x in numbers :
    if numbers[0] == numbers[-1] :
        if x != numbers[0] :
            final = x
    elif numbers[0] != numbers[-1]:
        if numbers[1] == numbers[0] :
            final = numbers[-1]
        elif numbers[1] != numbers[0] :
            final = numbers[0]
    
try:
    print(final)
except:
    print("All Are Same")
