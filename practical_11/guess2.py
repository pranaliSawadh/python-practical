import random
def initialization():
	print("Welcome to GUESS THE NUMBER")
	
	while True:
		entry_fees = float(input(" Enter the amount you want to pay as Entry fees: "))
		if entry_fees <= 0:
			print(" Please enter a valid positive number for the entry fees.\n")
		else:
			break

	reward = {'1':5*entry_fees , '2' : 3*entry_fees , '3': 2*entry_fees , '4' : 1.5*entry_fees , '5':entry_fees}
	print("you have 5 chances and for each chance you have particular reward\n")
	return reward
def guess_the_number():
	reward = initialization()
	number = random.randint(0,10)
	for chance in range(1,6):
		print(f"Chance {chance}")
		while True:
			entered_number = int(input("Guess the number from 0 to 10\n"))
			if 0 <= entered_number <= 10:
                    		break
			else:
                   		print("Please enter a valid number between 0 and 10.\n")
		
		if number==entered_number:
			reward_amount = reward[str(chance)]
			return f"congratulations you have entered correct number {number} on chance {chance} and You win: ₹{reward_amount}!"
	return f"better luck next time the number was {number}"
print(guess_the_number())
