import string
punc_list = [n for n in string.punctuation]
def pig_it(string):
    string_list = string.split(" ")
    string1 = ""

    for x in string_list :   
        if x in punc_list:
            string1 += x
            return string1
        else:
            index2 = x[0] 
            x += index2 + "ay"
            string1 += x[1:]
            string1 += " "         
    return string1[:-1]

print(pig_it("O tempora o mores !"))