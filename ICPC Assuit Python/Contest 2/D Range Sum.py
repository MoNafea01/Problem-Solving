'''
You are given a range represented by two integers L and R, and you should find the sum of the numbers in the range between L and R inclusive.

Input
First line contains a number T (1≤T≤105) – the number of test cases.
Each of the next T lines contains two numbers L,R (1≤L,R≤109).

Output
For each test case, print the sum.
'''
n = int(input())
lst = []
import math
while n:
    L,R = list(map(int,input().split()))
    sum_ = 0
    L,R = min(L,R),max(L,R)
    if L<R:
        lst.append((int(R) * int(R+1) - (int(L) * int(L-1))) //2)
    n-=1
[print(i) for i in lst]
