'''
Reverse every other word in a given string, then return the string. 
Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. 
Punctuation marks should be treated as if they are a part of the word in this kata.
'''




def reverse_alternate(string):
    if string == "":
        return ""
    if string.isspace() == True:
        return ""
    li = string.split(" ")
    li2 = []
    add = ""
    index = 0
    for x in li:
        if index % 2 == 1 :
            x = x[::-1]
            if x == "":
                continue
            else:
                li2.append(x)
        else:
            if x == "":
                continue 
            else:
                li2.append(x)
        index += 1
    pp = " ".join(li2)
    if pp.isspace() == True:
        return ""
    
    elif pp[-1].isspace() == True:
        pp[-1] = ""
    else:
        return  pp

print(reverse_alternate("s t r i n g"))