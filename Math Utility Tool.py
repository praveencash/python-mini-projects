import math

print("Welcome to Math Utility Tool")
print("1. Square Root")
print("2. Power")
print("3. Round Up")
print("4. Round Down")

choice = input("Choose an option (1-4): ")

if choice == '1':
    num = float(input("Enter a number: "))
    print("Square root of", num, "is", math.sqrt(num))

elif choice == '2':
    base = float(input("Enter base number: "))
    exponent = float(input("Enter exponent: "))
    print(f"{base} to the power of {exponent} is", math.pow(base, exponent))

elif choice == '3':
    num = float(input("Enter a number: "))
    print("Rounded up:", math.ceil(num))

elif choice == '4':
    num = float(input("Enter a number: "))
    print("Rounded down:", math.floor(num))

else:
    print("Invalid option. Please choose between 1 to 4.")