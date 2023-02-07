import random

print("Welcome to your Password Generator!\n")

allPasswords = []

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXWYZ!@#$%¨&*()1234567890'

number = input("Amount of password to generate: ")
number = int(number)

length = input("Input your password length: ")
length = int(length)

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    allPasswords.append(password)

print("\nHere are your password(s):\n")

for pwds in allPasswords:
    print(pwds)