# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    result = 3 * (a+b+c)
    print(f'Получается да, {result}')
else:
    print("не")