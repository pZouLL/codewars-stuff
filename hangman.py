import random
import time
words = ["gay" , "dancing" , "python" , "hangman" , "beautiful" , "online"
, "guessing" , "programming" , "coding" ]
 
word = random.choice(words)

lives = 5

li = ["_" for x in word]

while True:
    if "".join(li) == word:
        print("You Guessed it Right!")
        break

    if lives == 0 :
        print("You Failed, Please Try Again")
        break

    print(" ".join(li))
    print("Lives = ",lives)
    guess = input("Guess Letter: ")
    if guess in word:
        if guess == word:
            print("You Guessed it Right")
            break

        elif len(guess) == 1:
            for x in range(len(word)):
                if guess == word[x]:
                    li[x] = guess 

        else:
            print("1 Letter At A Time Or Guess The Whole Thing")
    
    else:
        print("That Is Incorrect")
        lives -= 1



