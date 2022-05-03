#Prompt:
'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
'''


#code:
def tickets(people):
    money25 = 0
    money50 = 0
    money100 =  0
    for x in people:
        if x == 25:
            money25 += 1
        elif x == 50:
            if money25 >= 1:
                money50 += 1
                money25 -= 1
            else:
                return "NO"
                break
        elif x == 100:
            if money25 > 0 and money50 > 0:
                money25 -= 1
                money50 -= 1
                money100 += 1
            elif money25 >= 3:
                money25 -= 3
                money100 += 1
            else:
                return "NO"
                break
    return "YES"




#Testings : 
'''
test.assert_equals(tickets([25, 25, 50]), "YES")
test.assert_equals(tickets([25, 100]), "NO")
'''