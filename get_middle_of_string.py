def even_or_odd(string):
    count = 0
    for i in string :
        count += 1    
    if count % 2 == 0 :
        return True
    else:
        return False

def get_count(string) :
    count1 =0
    for i in string:
        count1 += 1
    return count1

def make_list(string) :
    rist = []
    for i in string :
        rist.append(i)
    return rist
        



string1 = input("Input String : ")
itsevenomg = even_or_odd(string1)
countcount = get_count(string1)
listlist = make_list(string1)


if itsevenomg == True :
    num = countcount // 2 
    num2 = num - 1 
    index1 = listlist[num2]
    index2 = listlist[num]
    print(index1,index2)

if itsevenomg == False :
    num1 = countcount // 2
    index13 = listlist[num1]
    print(index13)
