while True:
    # everything goes inside here
	num = int(input("How many expenses do you want to enter? "))
	total = 0
	expenses = []
	for i in range(num):	
		expense = input(f"Enter the expense name {i+1}: ")
		amount = float(input(f"Enter the amount spent for {expense}: "))
		expenses.append((expense,amount))
		total += amount
	print(f"Total expenses: {total}")
	print("\nYour expenses:")
	for item in expenses:
		print(f"{item[0]} - Rs{item[1]}")
	again = input("Do you want to add more expenses? (yes/no): ")
	if again.lower() != "yes":
	    print("Thank you for using the Expense Tracker!")
	    break