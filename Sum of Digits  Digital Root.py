'''
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.

Examples
16  -->  1 + 6 = 7
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''
def digital_root(n):
    new = 0
    new2 =0
    for x in str(n):
        x = int(x)
        new += x
    if len(str(new)) >= 2:
        new1 = 0
        for i in str(new):
            i = int(i)
            new1 += i 
        while len(str(new1)) >= 2:
            for i in str(new1):
                i = int(i)
                new2 += i 
            return new2
        return new1
    
    else:
        return new