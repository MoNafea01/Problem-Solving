'''
Given a number N. Print the factorial of number N.

Input
First line contains a number T (1≤T≤15) number of test cases.
Next T lines will contain a number N (0≤N≤20)

Output
For each test case print a single line contains the factorial of N.
'''
cases = int(input())
while cases:
    n= int(input())
    f=1
    for i in range(2,n+1):
        f *= i
    print(f)
    cases -=1
