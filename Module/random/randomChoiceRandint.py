import random
import string

# print color in hex
color = "{:06x}".format(random.randint(0, 0xFFFFFF))
print("random color:", color)

# create an alphabetical string
word = ''.join(random.choices(list(string.ascii_letters), k=10))
print(word)

print(string.digits)

l = [i for i in range(1, 71) if i%7 == 0]
print(f"random number divisible by 7 between 1 & 70:", random.choice(l))
# print(f"random number divisible by 7 between 1 & 70:", (random.randint(0, 10))*7)1