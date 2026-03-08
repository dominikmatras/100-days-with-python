import random

friends = ["Dominik", "Adam", "Jacek", "Radek", "Marek"]
random_friend = random.randint(1, 5) - 1
print(f"Pay: {friends[random_friend]}")

print(random_friend)