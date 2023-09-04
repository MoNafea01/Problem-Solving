'''
Given N numbers. Count how many of these values are even, odd, positive and negative.

Input
First line contains one number N (1≤N≤103) number of values.
Second line contains N numbers (-105≤Xi≤105).

Output
Print four lines with the following format:
First Line: "Even: X", where X is the number of even numbers in the given input.
Second Line: "Odd: X", where X is the number of odd numbers in the given input.
Third Line: "Positive: X", where X is the number of positive numbers in the given input.
Fourth Line: "Negative: X", where X is the number of negative numbers in the given input.
'''
import numpy as np
x = int(input())
lst = list(map(int,input().split()))
lst=np.array(lst)
print(f'Even: {len(lst[lst%2==0])}')
print(f'Odd: {len(lst[lst%2==1])}')
print(f'Positive: {len(lst[lst>0])}')
print(f'Negative: {len(lst[lst<0])}')
