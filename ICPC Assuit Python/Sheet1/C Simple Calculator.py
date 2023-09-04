'''
Given two numbers X and Y. Print the summation and multiplication and subtraction of these 2 numbers.

Input
Only one line containing two separated numbers X, Y (1  ≤  X, Y  ≤  105).

Output
Print 3 lines that contain the following in the same order:

X + Y = summation result" without quotes.
X * Y = multiplication result" without quotes.
X - Y = subtraction result" without quotes.
'''
x = input().split()
x = [ int(i) for i in x]
print(f"{x[0]} + {x[1]} = {x[0]+x[1]}")
print(f"{x[0]} * {x[1]} = {x[0]*x[1]}")
print(f"{x[0]} - {x[1]} = {x[0]-x[1]}")
