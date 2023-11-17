from time import sleep
import random

print("Entering into lottery winner selection:")

tickets = []
for i in range(100):
    tickets.append(random.randrange(100000, 999999))

print("Selecting winners:")
winner = random.sample(tickets, k=3)

print("Please wait...")
sleep(3)

print(f"First: {winner[0]}\nSecond: {winner[1]}\nThird: {winner[2]}")
