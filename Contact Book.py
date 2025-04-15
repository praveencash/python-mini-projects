contacts = {}
while True:
	print('Contact Book')
	print('1. Add Contact')
	print('2. View all Contacts')
	print('3. Search Contact')
	print('4. Delete Contact')
	print('5. Exit')
	choice = input("Choose an option: ")
	if choice =='1':
		name = input('Enter the Name: ')
		phone = input('Enter the phone number: ')
		contacts[name.upper()] = phone
		print('Contact added successfully!')
	elif choice == '2':
		if not contacts:
			print('No contacts found!')
		else:
			for name, phone in contacts.items():
					print(f'{name} : {phone}')
	elif choice == '3':
		search_name = input("Enter the name to search: ")
		if search_name.upper() in contacts:
			print(f"{search_name.upper()} : {contacts[search_name.upper()]}")
		else:
			print('Contact not found!')
	elif choice == '4':
		delete_name = input("Enter the name to delete: ")
		if delete_name.upper() in contacts:
			del contacts[delete_name.upper()]
			print("Contact deleted successfully!")
		else:
			print('Contact not found!')
	elif choice == '5':
		print('Thank you for using Contact Book!')
		break
	else:
		print('This is not a valid option. Try again!')
		