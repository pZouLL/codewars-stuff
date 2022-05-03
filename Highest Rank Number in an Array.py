'''
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
'''

def highest_rank(arr):
    dict = {}
    check = 0
    for x in arr: 
        if x not in dict: dict[x] = 1
        else: dict[x] += 1
    li = [key for key,value in dict.items() if value == max(dict.values())]
    return max(li)

print(highest_rank([10, 12, 8,8, 12, 12,8, 6, 4, 10, 10]))