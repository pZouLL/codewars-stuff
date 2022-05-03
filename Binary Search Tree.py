import random
def binary_search_tree(array , target):
    array.sort()
    top = len(array)
    low = 0 

    while True:
        middle = (top + low) // 2
        if array[middle] == target:
            return middle

        elif array[middle] > target:
            top = middle 
        elif array[middle] < target:
            low = middle 

array = []
for x in range(10000):
    print(x)
    array.append(random.randint(1,100000000))

target = random.choice(array)

for x in array:
    if x == target:
        print(x)

            