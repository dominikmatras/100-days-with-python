print("Welcome to Pyhton Pizza Delivery!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? ")
extra_chesse = input("Do you want extra chesse? ")

# S - 15, M - 20, L - 25. 
# P (S) - 2, P (M, L) - 3
# C - 1

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pepperoni_small_price = 2
pepperoni_medium_large_price = 3
extra_chesse_price = 1

bill = 0

if size == "S":
  bill += small_pizza_price
  if pepperoni == "Y":
    bill += pepperoni_small_price
elif size == "M":
  bill += medium_pizza_price
  if pepperoni == "Y":
    bill += pepperoni_medium_large_price
else:
  bill += large_pizza_price
  if pepperoni == "Y":
    bill += pepperoni_medium_large_price

if extra_chesse == "Y":
  bill += extra_chesse_price

print(f"Your finall bill is: ${bill}")