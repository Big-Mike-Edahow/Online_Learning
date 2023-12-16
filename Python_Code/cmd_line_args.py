# cmd_line_args.py

import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg

print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(int(first_number) + int(second_number))

parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")

