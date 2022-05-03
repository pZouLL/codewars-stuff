'''
Your task is to write function findSum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)

testing:
test.assert_equals(find(5), 8)
test.assert_equals(find(10), 33)
'''

def find(n):
    add = 0
    for x in range(1,n+1):
        print(add)
        if x % 3 == 0 :
            add += x
        elif x % 5 == 0:
            add += x
        else:
            continue
    return add
