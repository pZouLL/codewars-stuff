'''
+1 Array
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples
For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]
'''

'''
OLD CODE :
def up_array(arr):
    number = "" 
    li=[]
    if arr == []:
        return None 
    elif arr == None:
        return None 
    else:
        for x in arr:
            if x < 0:
                return None 
            elif x >= 10 :
                return None

        for i in arr :
            i = str(i)
            number += i
        
        number = int(number)
        number += 1 

        for t in str(number):
            t = int(t)
            li.append(t)
        
        return li
'''

#NEW CODE:

def up_array(arr):
    if arr == [] or arr == None or [True for x in arr if x < 0] or [True for x in arr if x > 9]  : return None
    return [int(x) for x in str(int("".join([str(x) for x in arr])) + 1)]

print(up_array([1,2,3]))






    


