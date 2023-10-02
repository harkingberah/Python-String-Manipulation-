# User Input
user_string = input("Enter a string: ")

# String Operations Menu
print("\nString Operations Menu:")
print("1. Count characters")
print("2. Reverse the string")
print("3. Check for palindrome")
print("4. Convert to uppercase")
print("5. Convert to lowercase")
print("6. Find specific character")
print("7. Exit")

# Get user's choice
choice = input("Select an operation (1-7): ")

# Perform the selected string operation
if choice == '1':
    print(f"Number of characters: {len(user_string)}")
elif choice == '2':
    print(f"Reversed string: {user_string[::-1]}")
elif choice == '3':
    if user_string == user_string[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
elif choice == '4':
    print(f"Uppercase: {user_string.upper()}")
elif choice == '5':
    print(f"Lowercase: {user_string.lower()}")
elif choice == '6':
    char_index = int(input("Enter the character index to find: "))
    if char_index >= 0 and char_index < len(user_string):
        print(f"Character at index {char_index}: {user_string[char_index]}")
    else:
        print("Invalid index.")
elif choice == '7':
    print("Goodbye!")
else:
    print("Invalid choice. Please select a valid operation.")
