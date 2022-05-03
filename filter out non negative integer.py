#filter out non negative integer
'''
def filter_list(thelist):
    mainlist = []
    for x in thelist:
        if type(x) == int:
            mainlist.append(x)
    return mainlist
'''

def filter_list(thelist):
    mainlist = [x for x in thelist if type(x) == int if x >= 0]
    return mainlist
    


print(filter_list([1,2,'a','b' , -1]))