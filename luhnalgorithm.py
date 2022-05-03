'''
creditcardvalidator(luhnalgo)

In this Kata, you will implement the Luhn Algorithm, which is used to help validate credit card numbers.

Given a positive integer of up to 16 digits, return true if it is a valid credit card number, and false if it is not.

Here is the algorithm:

Double every other digit, scanning from right to left, starting from the second digit (from the right).

Another way to think about it is: if there are an even number of digits, double every other digit starting with the first; if there are an odd number of digits, double every other digit starting with the second:

1714 ==> [1*, 7, 1*, 4] ==> [2, 7, 2, 4]

12345 ==> [1, 2*, 3, 4*, 5] ==> [1, 4, 3, 8, 5]

891 ==> [8, 9*, 1] ==> [8, 18, 1]
If a resulting number is greater than 9, replace it with the sum of its own digits (which is the same as subtracting 9 from it):

[8, 18*, 1] ==> [8, (1+8), 1] ==> [8, 9, 1]

or:

[8, 18*, 1] ==> [8, (18-9), 1] ==> [8, 9, 1]
Sum all of the final digits:

[8, 9, 1] ==> 8 + 9 + 1 = 18
Finally, take that sum and divide it by 10. If the remainder equals zero, the original credit card number is valid.

18 (modulus) 10 ==> 8 , which is not equal to 0, so this is not a valid credit card number

'''

def validate(n , NEWADD = 0 , the_lord_list = [] , new_lord = [] , newlordthistime = [] , addd = 0):
    for x in str(n):
        x = int(x)
        the_lord_list.append(x)
    
    if len(the_lord_list) % 2 == 0 :
        index = 0 
        for i in the_lord_list:
            if index % 2 == 0 :
                new_lord.append(i*2)
                index += 1
            else:
                index +=1
                new_lord.append(i)
    else:
        index = 0 
        for i in the_lord_list:
            if index % 2 == 1:
                new_lord.append(i*2)
                index +=1
            elif index % 2 == 0:
                index +=1
                new_lord.append(i)
                
    for p in new_lord:
        if p > 9:
            for xd in str(p):
                xd = int(xd)
                addd += xd
            newlordthistime.append(addd)
        else:
            newlordthistime.append(p)
            
    for o in newlordthistime:
        NEWADD += o
    
    if NEWADD % 10 == 0:
        return True
    else:
        return False
