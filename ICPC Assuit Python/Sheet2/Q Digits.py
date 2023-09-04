'''
Given a number N. Print the digits of that number from right to left separated by space.

Input
First line contains a number T (1≤T≤10) number of test cases.
Next T lines will contain a number N (0≤N≤109)

Output
For each test case print a single line contains the digits of the number separated by space.
'''
x = int(input())
for i in range(x):
    inp = input()
    inp = list(reversed(inp))
    print(*inp)
