'''
A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more characters. The 1st character of a code is a capital letter which defines the book category.

In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

For example an extract of a stocklist could be:

L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
or
L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :

M = {"A", "B", "C", "W"} 
or
M = ["A", "B", "C", "W"] or ...
and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.

For the lists L and M of example you have to return the string (in Haskell/Clojure/Racket a list of pairs):

(A : 20) - (B : 114) - (C : 50) - (W : 0)
where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.

If L or M are empty return string is "" (Clojure and Racket should return an empty array/list instead).

Note:
In the result codes and their values are in the same order as in M.

testing:
b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")

'''
def stock_list(b,c):
    count = 1
    quantity_lii = []
    booktype = "" 
    number_new = ""
    if b == [] or c == []:
        return ""

    for i in b:
        for x in i: 
            if x in ["1","2","3","4","5","6","7","8","9","0"] : 
                number_new += x 
                if count == len(i):
                    number_new = int(number_new)
                    quantity_lii.append(number_new)
                    number_new = ""
                    count = 0
            else:
                booktype += x 
            count +=1

    booktype_str = booktype.split(" ")
    booktype_int = [x[0] for x in booktype_str[:-1]]

    new_dict = {}
    for x in range(len(quantity_lii)):
        if booktype_int[x] in new_dict:
            new_dict[booktype_int[x]] += quantity_lii[x]
        else:
            new_dict[booktype_int[x]] = quantity_lii[x]

    pick_out_category_in_c= {}
    for cat in c:
        if cat in new_dict:
            pick_out_category_in_c[cat] = new_dict[cat]
        else:
            pick_out_category_in_c[cat] = 0

    final_string = str(pick_out_category_in_c)
    final_li = final_string.replace("'" , "").replace("{" , "").replace("}","").replace(" " , "").replace(":" , "").split(",")
    final_output = ""
    for d in final_li:
        for i in d:
            if i in ["1","2","3","4","5","6","7","8","9"]:
                for x in final_li:
                    final_output += "({} : {}) - ".format(x[0] , x[1:])
                return final_output[:-3]  
    return ""