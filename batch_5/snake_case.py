# Ask the user to input their fullname in incorrect casing. Print the input in snake case.
fullname = input("Enter your fullname with incorrect casing: ")
print("_".join(fullname.lower().split()))