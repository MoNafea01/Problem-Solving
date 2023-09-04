'''
Given two numbers X and Y. Print the sum of all odd numbers between them, excluding X and Y.

Input
First line contains a number T (1≤T≤10) number of test cases.
Next T lines will contain two numbers X and Y (0≤X,Y≤104).

Output
Print the sum of all odd numbers between X and Y (excluding X and Y).
'''
n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    x,y = min(x,y),max(x,y)
    sum_ = 0
    for j in range(x+1,y):
        if j%2 !=0:
            sum_ +=j
    print(sum_)
