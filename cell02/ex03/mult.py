#!/usr/bin/env python3

first_number = float(input("Enter the first number:\n"))
second_number = float(input("Enter the second number:\n"))

result = first_number * second_number

print(f"{first_number:g} x {second_number:g} = {result:g}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
