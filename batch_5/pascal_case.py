# Ask the user to input their fullname in incorrect casing. Print the input in pascal case.
fullname = input("Enter your fullname with incorrect casing: ")
print("".join(word.capitalize() for word in fullname.split()))