
'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

import codewars_test as test
from solution import move_zeros

@test.it("Basic tests")
def youarecute():
    test.assert_equals(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    test.assert_equals(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    test.assert_equals(move_zeros([0, 0]), [0, 0])
    test.assert_equals(move_zeros([0]), [0])
    test.assert_equals(move_zeros([]), [])

'''

def move_zeros(array):
    all_zero_index = []
    for index , num in enumerate(array):
        if num == 0:
            all_zero_index.append(index)

    print(all_zero_index)
    thing = 0 
    for index in all_zero_index:
        array.pop(int(index)-thing)
        array.append(0)
        thing += 1


    return array


