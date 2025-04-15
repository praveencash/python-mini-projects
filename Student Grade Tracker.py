grades = {}
while True:
	print('Tracker book')
	print('1. Add Student')
	print('2. View all students')
	print('3. Update Grade')
	print('4. Delete Student')
	print('5. Exit')
	option = input('Enter your option(1/2/3/4/5): ')
	if option == '1':
		name = input('Enter the Student name: ')
		grade = input('Enter the Student grade: ')
		grades[name.upper()] = grade.upper()
		print('Student added successfully')
	elif option == '2':
		if not grades:
			print('No students found!')
		else:
			for name, grade in grades.items():
				print(f'{name} : {grade}')
	elif option == '3':
		name = input('Enter the student name to update: ')
		if name.upper() in grades :
			new_grade = input('Enter the new grade: ')
			grades[name.upper()] = new_grade.upper()
			print('Grade updated successfully!')
		else:
			print('Student not found!')
	elif option == '4':
		name = input('Enter the student data you want to delete: ')
		if name.upper() in grades:
			del grades[name.upper()]
			print('Student data erased successfully!')
		else:
			print('Student not found!')
	elif option == '5':
		print('Thank you for using Tracker!')
		break
	else:
		print('Not an valid option. Please try again!')
		