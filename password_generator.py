# Password Generator

import random
import string

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password =[]

for i in range(0,nr_letters):
    randomLetter = random.choice(string.ascii_letters)
    password.append(randomLetter)

# for j in range(0,nr_symbols):
    symbol = random.choice(symbols)
    password.append(symbol)

for k in range(0,nr_numbers):
    numberrandom = str(random.randint(0,9))
    password.append(numberrandom)


# print(password)

total_char = nr_numbers + nr_letters + nr_symbols

random_list = random.sample(password, total_char)
result = ''.join(map(lambda x: x, random_list))
print(f'Your Password is: {result}')