def is_leap(year):
    bagi_4 = year / 4
    bagi_s = str(bagi_4)
    
    bagi_100 = year / 100
    bagi_s1 = str(bagi_100)
    
    bagi_400 = year / 400
    bagi_s2 = str(bagi_400)
    if bagi_s[-1] == "0" and bagi_s1[-1] == "0" and bagi_s2[-1] == "0" :
        return True
    elif bagi_s[-1] == "0" and bagi_s1[-1] != "0" and bagi_s2[-1] != "0" :
        return True
    else:
        return False

year = int(input("Input : "))
print(is_leap(year))