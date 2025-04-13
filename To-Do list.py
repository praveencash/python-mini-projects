tasks = []
while True:
	print('Welcome to the To-Do list App!')
	print('1. Add a task')
	print('2. View tasks')
	print('3. Delete a task')
	print('4. Exit')
	choice = input('Please choose between options: 1/2/3/4 ')
	if choice == '1':
		task = input('Enter the task: ')
		tasks.append(task)
		print('Task added!')
	elif choice == '2':
		if not tasks:
			print("No tasks available!")
		else:
			print('Your tasks:')
			for i, t in enumerate(tasks, start = 1):
				print(f'{i}. {t}')
	elif choice == '3':
		task_num = int(input('Which task you want to delete: '))
		if 0 < task_num <= len(tasks):
			tasks.pop(task_num - 1)
			print('Task Deleted!')
		else:
			print('Invalid Task Number!')
	elif choice == '4':
		print('Thanks for using the To-Do list app!')
		break
	else:
		print('Invalid option chosen. Please choose again')