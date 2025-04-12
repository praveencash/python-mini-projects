
while True:
	quiz_1 = input("What is the capital of India? ")
	score = 0
	if quiz_1.lower() == 'delhi':
	   		print("Correct")
	   		score +=1
	else:
	   	print('Wrong')
	quiz_2 = input("What is the capital of Tamilnadu? ")
	if quiz_2.lower() == "chennai":
	   	print("Correct")
	   	score +=1
	else:
	  	print("Wrong")
	quiz_3 = input("What is the national animal of India? ")
	if quiz_3.lower() == "tiger":
	  	print("Correct")
	  	score += 1
	else:
	      print("Wrong")
	quiz_4 = input("What is the favorite sport of Indians? ")
	if quiz_4.lower() == "cricket":
	  	print("Correct")
	  	score += 1
	else:
	  print("Wrong")
	quiz_5 = input("Name any one neighbor of India: ")
	if quiz_5.lower() in [ "pakistan","china", "bhutan","srilanka", "nepal", "afghanistan"] :
	  	print("Correct")
	  	score += 1
	else:
		print("Wrong")
		
	print(f"You got {score} out of 5 correct!")
	if score == 5:
	  print("Excellent!")
	elif score >= 3:
	  print("Good job!")
	else:
	  print("Better luck next time!")
	  
	play_again = input("Do you want to try the quiz again? (yes/no): ")
	if play_again.lower() != "yes":
	       print("Thanks for playing!")
	       break