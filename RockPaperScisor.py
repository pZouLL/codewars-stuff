#python C:\Users\Win10\Desktop\Coding\Python\OutsideSchool\RockPaperScisor.py

import random
loop = 1
char = ["Rock" , "Paper" , "Scissor"]




while loop == 1:
	print("")
	print("Rock Paper Scisor ")
	print("")
	pick = input("Play? (Y/N) : ")

	if pick == "Y" :
		bot = random.choice(char)
		print(bot)
		user = input("Rock , Paper  Or Scisor? (R/P/S) : ")

		#Rock
		if bot == "Paper" and user == "P" :
			print("Tie , You Both Picked Paper")

		if bot == "Paper" and user == "R" :
			print("You Lost , Bot Picked Paper")

		if bot == "Paper" and user == "S" :
			print("You Won , Bot Picked Paper")

		#Paper
		if bot == "Rock" and user == "R" :
			print("Tie, You Both Picked Rock")

		if bot == "Rock" and user == "P" :
			print("You Won, Bot Picked Rock")

		if bot == "Rock" and user == "S" :
			print("You Lost, Bot Picked Rock")

		if bot == "Scissor" and user == "P" :
			print("You Lost, Bot Picked Scissor")

		if bot == "Scissor" and user == "R" :
			print("You Won, Bot Picked Scissor")

		if bot == "Scissor" and user == "S" :
			print("Tie, You Both Picked Scissor")


	if pick == "N" :
		exit()