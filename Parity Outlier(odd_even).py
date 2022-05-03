l = [2, 4, 0, 100, 4, 11, 2602, 36]

if l[0] % 2 == 0 and l[-1] % 2 == 0 :
    for x in l :
        if x % 2 != 0 :
            print(x)

if l[0] % 2 != 0 and l[-1] % 2 != 0 :
    for x in l :
        if x % 2 == 0 :
            print(x)

if l[0] % 2 != 0 and l[-1] % 2 == 0 :
    if l[1] % 2 == 0 :
        print(l[0])
    elif l[1] % 2 != 0 :
        print(l[-1])

if l[-1] % 2 != 0 and l[0] % 2 == 0 :
    if l[1] % 2 == 0 :
        print(l[-1])
    elif l[1] % 2 != 0 :
        print(l[0])
