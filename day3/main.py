print("Welcome in the game ;)")
print("You mission is escape form house in fire!")
print("")
print("You house is in fire! Run!!")
# Inputs
first_decision = input("You leave your room. Where do you want to go? (type 'left' or 'right')\n ")
second_decision = input("You reach the stairs. Do you go down or keep going? (type 'down' or 'keep') \n ")
third_decision = input("There is fire everywhere, do you escape through the door, the garage or the window? (type 'door', 'garage' or 'window')\n ")

game_over = 0

if first_decision == 'left': 
  game_over = 1
  print("Game Over!")

if second_decision == 'keep':
  game_over = 1
  print("Game Over!")

if third_decision == 'door' and third_decision == 'garage':
  game_over = 1
  print("Game Over!")

if game_over != 1:
  print("You escaped!")