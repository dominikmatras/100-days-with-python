import random

print("Kamień, papier, noyżyce.. Podejmiesz się wyzwania?")
print("Wybierz od 0 - 2 (0 - kamień, 1 - papier, 2 - nożyce)")

user_number = int(input(""))
computer_number = random.randint(0, 2)

list_of_choice = ['kamień', 'papier', 'nożyce']

print(f"Wybrałeś: {list_of_choice[user_number]}")
print(f"Komputer wybrał: {list_of_choice[computer_number]}")
 
if user_number == 0 and computer_number == 2:
  print("Wygrałeś!")
elif computer_number == 0 and user_number == 2:
  print("Przegrałeś!")
elif computer_number > user_number:
  print("Przegrałeś!")
elif user_number > computer_number:
  print("Wygrałeś!")
elif computer_number == user_number:
  print("It's a draw")
else:
  print("Nieprawidłowy znak, przegrałeś!")
