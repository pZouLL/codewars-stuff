'''
Rules
 1.  The input string will always be lower case but maybe empty.

 2.  If the character in the string is whitespace then pass over it as if it was an empty seat

Example

wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

@test.describe('Example Tests')

def example_tests():
    result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case1():
        test.assert_equals(wave("hellodef wave(people,index = 0 , li = [],new_li=[]):
    for i in range(0,len(people)):
        li.append(people)
    for x in li:
        x = x.replace(x[index],x[index].upper())
        new_li.append(x)
        index += 1
    return new_li

print(wave("hello"))"), result)
    
    result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case2():
        test.assert_equals(wave("codewars"), result)
    
    result = []
    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case3():
        test.assert_equals(wave(""), result)
    
    result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case4():
        test.assert_equals(wave("two words"),result)
    
    result = [" Gap ", " gAp ", " gaP "]
    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case5():
        test.assert_equals(wave(" gap "), result)

'''
def wave(people):
    if people == "" or people == None:
        return []
    li = []
    new_li = []
    for x in people:
        li.append(x)
    for i in range(0,len(people)):
        if li[i] == " ":
            pass
        else:
            li[i] = li[i].upper()
            index = ""
            for p in li:
                index = index + p
            new_li.append(index)
            li[i] = li[i].lower()
    return new_li

print(wave("sixty nine"))