import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for letter in range(0, nr_letters):
  password_list.append(letters[random.randint(0, len(letters) - 1)])

for symbol in range(0, nr_symbols):
  password_list.append(symbols[random.randint(0, len(symbols) - 1)])

for number in range(0, nr_numbers):
  password_list.append(numbers[random.randint(0, len(numbers) -1 )])

print(f"\nGenerated list of items:\n{password_list}")

# Easy level

# final_password = ""
# for element in password_list:
#   final_password += str(element)



random.shuffle(password_list)

print("\nShuffle list of items:")
print(password_list)
print("")

final_password = ""
for element in password_list:
  final_password += str(element)

print(f"You pasword: {final_password}")