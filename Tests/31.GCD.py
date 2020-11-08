# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

a = int(input())
b = int(input())
while b:
    a, b = b, a % b
print(a, " - НОД")
