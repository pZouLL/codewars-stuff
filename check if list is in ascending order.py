#check if its in ascending order

def in_asc_order(arr) :
    for x in range(0,len(arr)-1):
        if arr[x] < arr[x + 1]:
            continue
            
        else:
            return False
            break
    return True

'''
#testings:
test.describe("Example Tests")
# Array of 2 integers
arr =     
test.assert_equals(in_asc_order(arr), True)

arr = [2, 1]
test.assert_equals(in_asc_order(arr), False)

# Array of 3 integers
arr = [1, 2, 3]
test.assert_equals(in_asc_order(arr), True)

arr =     
test.assert_equals(in_asc_order(arr), False)

# More complex cases
arr = [1,4,13,97,508,1047,20058]
test.assert_equals(in_asc_order(arr), True)

arr = [56,98,123,67,742,1024,32,90969]
test.assert_equals(in_asc_order(arr), False)
'''
