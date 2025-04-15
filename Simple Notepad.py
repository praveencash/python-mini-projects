while True:
	print('Simple Notepad')
	print('1. Add a note')
	print('2. View notes')
	print('3.Exit')
	choice = input('Please choose the option you need to use(1/2/3): ')
	if choice == '1':
		note = input("Type your note: ")
		with open('notes.txt', 'a') as file:
			file.write(note + '\n')
			print('Note saved!')
	elif choice == '2':
				with open('notes.txt', 'r') as file:
						content = file.read()
						print('\nYour notes: \n')
						print(content)
						if content.strip() == "":
								print('No notes yet')
	elif choice == '3':
		print('Thank you for using Notepad! Have a great day!')
		break
	else:
		print('Invalid option selected. Try again!')
		