import random
def guess_the_number():
	number = random.randint(0,10)
	
	print("Guess the number from 0 to 10")
	entered_number = input()
	if int(entered_number) in range(11):
		if int(entered_number)==number:
			return "Congratulation You have guessed the correct number : {}"
		else:
			return f"Better luck next time!!! \n You have guessed the wrong number , the number was {number}"
	else:
		return "Enter the valid number between given range"
print(guess_the_number())
