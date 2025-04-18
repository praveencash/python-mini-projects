score = 0

def ask_question(question, answer):
    global score
    try:
        user_input = input(question + " ").strip().lower()
        if user_input == "":
            print("You didn’t type anything!")
            return
        if user_input == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    except Exception as e:
        print("Something went wrong:", e)

# Questions
ask_question("What is the capital of India?", "Delhi")
ask_question("What is the capital of Tamilnadu?", "Chennai")
ask_question("What is the national animal of India?", "Tiger")
ask_question("What is the favourite sport of Indians?", "Cricket")
ask_question("Name any one neighbour of India?", "Pakistan")

# Final score
print(f"\nYou got {score} out of 5 correct!")

# Retry option
while True:
    try:
        retry = input("Do you want to try the quiz again? (yes/no): ").strip().lower()
        if retry == "yes":
            print("\nRestart the quiz to play again!")
            break
        elif retry == "no":
            print("Thanks for playing!")
            break
        else:
            print("Please type yes or no.")
    except:
        print("Something went wrong with your input.")