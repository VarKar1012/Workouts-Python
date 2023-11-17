import random

firstname = ['devin', 'dainty', 'abin', 'jessica', 'ashna', 'afitha']
lastname = ['mathew', 'mathew', 'eldhose', 'joseph', 'hassif', 'jabbar']
streetname = ['high', 'low', 'lose', 'hola', 'warks', 'rody']
states = ['AL', 'KL', 'ML', 'CP', 'EK', 'DL']
fakecities = ['logsow', 'florida', 'poland', 'germany', 'prague', 'austria']

print("Here's your fake addresses:")
for i in range(10):
    first = random.choice(firstname)
    last = random.choice(lastname)
    name = f"{first} {last}".title()

    email = first + last + '@gmail.com'

    phone = f'+91-{random.randrange(100000000, 999999999)}'

    street = random.choice(streetname)
    state = random.choice(states)
    city = random.choice(fakecities)
    zipcode = random.randrange(10000, 50000)
    address = f"{street}, {city}, {state}, {zipcode}"

    print(f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}")
    print()