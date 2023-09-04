'''
Given two numbers N and M. Print the summation of their last digits.

Input
Only one line containing two numbers N, M (0 ≤ N, M ≤ 1018).

Output
Print the answer of the problem.
'''
x,y = list(map(int,input().split()))
print(x % 10 + y % 10)
