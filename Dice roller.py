import random
while True:
	print('Welcome to dice game!')
	choice = input("Roll again:(yes/no) ")
	if choice.lower() == 'yes':
		roll = random.randint(1,6)
		print(f'You have rolled: {roll}')
	elif choice.lower() == 'no':
		print('Thank you for playing!')
		break
	else:
		print('Invalid choice. Please try again!')
	
		
	