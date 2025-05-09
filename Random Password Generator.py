import random
import string
length = int(input("How long should the password be? "))
all_chars = string.ascii_letters + string.digits + string.punctuation
password = random.choices(all_chars, k=length)
final_password = ''.join(password)
print("Your random password is:", final_password)