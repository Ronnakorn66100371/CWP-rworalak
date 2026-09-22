#!/usr/bin/env python3

first_number = float(input("Give me the first number: "))
second_number = float(input("Give me the second number: "))

print("Thank you!")
print(f"{first_number:g} + {second_number:g} = {first_number + second_number:g}")
print(f"{first_number:g} - {second_number:g} = {first_number - second_number:g}")
if second_number == 0:
    print(f"{first_number:g} / {second_number:g} = Cannot divide by zero.")
else:
    print(f"{first_number:g} / {second_number:g} = {first_number / second_number:g}")
print(f"{first_number:g} * {second_number:g} = {first_number * second_number:g}")
