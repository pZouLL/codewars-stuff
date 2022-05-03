words = ["apple", "banana", "clock", "potato",
         "patch", "kiwi", "watch", "plum", "catch",
         "rambutan", "orang utan", "dock", "chip"]

search = input("Enter some letters: ")

def search1(letter) :    
    matches = []
    for word in words:
        if letter in word:
            matches.append(word)
    return matches

print(search1(search))