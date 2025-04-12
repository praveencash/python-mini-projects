while True:
	first_num = float(input("Enter the first number: "))
	second_num = float(input("Enter the second number: "))
	operation = input("Enter the operation needed to perform : (*,/,+,-) ")
	if operation == '+':
		result = first_num + second_num
	elif operation == '*':
		result = first_num * second_num
	elif operation == '-':
		result = first_num - second_num
	elif operation == '/':
	       if second_num == 0:
	       	 print("Error: Cannot divide by zero.")
	       	 continue
	       result = first_num / second_num
	else:
		print("This is just a basic calculator. This will perform only +,-,*,/. Try again")
		continue
	
	print(f"Result = {result}")
	again = input("Do you want to perform another calculation? (yes/no): ")
	if again.lower() != "yes":
	     print("Thank you for using the calculator!")
	     break