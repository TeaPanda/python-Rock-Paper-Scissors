import random

'''1 = rock
2 = paper
3 = scissors '''

result = 0

while True:
	while True:
		print("What would you like to choose?")
		print("Say 'S' for Scissors 'P' for Paper and 'R' for Rock ")
		choice = input()
		out = random.randint(1,3)
		choice = choice.capitalize()
		if choice == "S":
			print("You chose Scissors")
			break
		elif choice == "P":
			print("You chose Paper")
			break
		elif choice == "R":
			print("You chose Rock")
			break
		else:
			print("Please just answer 'S','P' or 'R'")
			continue

	if ((choice == "S") and (out == 3)) or ((choice == "P") and (out == 2)) or ((choice == "R") and (out == 1)):
		print("It's a DRAW")
		result = 0
	elif ((choice == "S") and (out == 2)) or ((choice == "P") and (out == 1)) or ((choice == "R") and (out == 3)):
		print("You WIN")
		result += 1
	else:
		print("You LOSE")
		result -= 1

	print("You score so far is " + str(result))
	print("Press any key to keep playing")
	input()
