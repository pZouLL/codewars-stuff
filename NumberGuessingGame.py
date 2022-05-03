
from random import randint

loop = 1
while loop == 1 :
	yesno = input("Play? (Y/N) : ")
	loop1 = 1
	while loop1 == 1 :
		if yesno == "Y":
			pick = int(input("Input Random Number From :"))
			pick2 = int(input("Input Random Number To : "))
			number = randint(pick , pick2)
			print("You Have 5 Lives")
			print("Number is From" , pick , "To" , pick2 , " Good Luck")
			lives = 5
			loop2 = 1
			while loop2 == 1 :
				guess = int(input("Guess Whats The Number: "))

				if guess == number :
					 print("Congratulations You Won")
					 loop2 = 2
					 loop1 = 2

				if guess != number :
					print("Wrong Guess , Try Again")
					lives = lives - 1 
					if lives == 2 :
						checker = number % 3 
						if checker == 0 :
							print("Number is divisible by 3")
						if checker != 0 :
							print("number is not divisible by 3")
								
				if lives == 0 :
					print("")
					print("Failed")
					print("The Number Was:" , number)
					print("")
					loop2 = 2
					loop1 = 2


	
	if yesno == "N" :
		exit()
