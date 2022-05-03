number = [19, 5, 42, 2, 77]

smallest = number[0]
for x in number :
    if x < smallest :
        smallest = x


smallest1 = number[0]
for i in number :
    if i < smallest1 and i != smallest :
        smallest1 = i

print(smallest + smallest1)
