'''
Given a number N, and N numbers, find maximum number in these N numbers.

Input
First line contains a number N (1≤N≤103).
Second line contains N numbers Xi (0≤Xi≤109).

Output
Print the maximum number.
'''
x=input()
y = list(map(int,input().split()))
print(max(y))
