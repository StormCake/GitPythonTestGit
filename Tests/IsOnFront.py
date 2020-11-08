# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

string = str(input())
if string[0:2] != 'Is':
    string = "Is" + string
print(f'{string}')
print(id(string))