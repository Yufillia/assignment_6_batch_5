# Ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
fullname = input("Enter your fullname with incorrect casing: ")
print("".join([char.upper() if char.islower() else char.lower() for char in fullname]))