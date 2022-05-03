n = int(input("Number : "))
step , loop = 0 , 1
print(f"Step 0 : {n}\n")
while loop == 1 :
    if n > 1 :
        if n % 2 == 0 :
            step += 1
            n = n / 2
            print(f"Step {step} : {n}\n")
            if n == 1 : loop = 2      

        elif n % 2 == 1 :
            step += 1
            n = n * 3 + 1
            print(f"Step {step} : {n}\n")
            if n == 1 : loop = 2       

    else: break