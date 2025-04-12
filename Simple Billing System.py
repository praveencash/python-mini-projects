from datetime import datetime
while True:
	current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	print(f"Date & Time: {current_time}")
#price of each items
	coffee_price = 120
	sandwich_price =150
	juice_price = 100
#menu card
	print("Welcome to JP Cafe")
	print("\tMenu")
	print(f"1. Coffee    - {coffee_price}")
	print(f"2. Sandwich  - {sandwich_price}")
	print(f"3. Juice     - {juice_price}")
	while True:
	    	try:
	    		coffee_qty = int(input("How many coffees you need:"))
 	   		break
 	   	except ValueError:
	       	 print("Type a valid number.")
	while True:
			try:
	 	         sandwich_qty = int(input("How many sandwiches you want:"))
	 	         break
			except ValueError:
			     print("Type a valid number.")
	while True:
			try:  	
			     juice_qty = int(input("How many juices you need:"))
			     break
			except ValueError:
				print("Type a valid number.")
  
	coffee_tot = coffee_qty * coffee_price
	sandwich_tot = sandwich_qty * sandwich_price
	juice_tot = juice_qty * juice_price
	total = coffee_tot + sandwich_tot + juice_tot

	if total > 500:
		discount = total * 0.1
	else:
		discount = 0

	final_bill = total - discount

	name = input("Enter your name: ")
	print(f"\nCustomer Name: {name}")
	gst = final_bill * 0.05
	final_amount_with_gst = final_bill + gst
	total_items = coffee_qty + sandwich_qty + juice_qty
	print(f"Total Items Ordered: {total_items}")
	if coffee_qty > 0:
		print(f"Coffee × {coffee_qty} = {coffee_tot}")
	if sandwich_qty > 0:
		print(f"Sandwich × {sandwich_qty} = {sandwich_tot}")
	if juice_qty > 0:
		print(f"Juice × {juice_qty} = {juice_tot}")
	print(f"Total before discount : {total}")
	print(f"Discount: {discount}")
	print(f"Subtotal: {final_bill}")
	print(f"GST(5%): {gst}")
	print(f"Final Bill: {final_amount_with_gst}")
	print("\nThank you for visiting JP Cafe! Have a great day!")
	again = input("\nDo you want to place another order? (yes/no): ")
	if again.lower() != "yes":
		print("Thank you for ordering with JP Cafe!")
		break
	