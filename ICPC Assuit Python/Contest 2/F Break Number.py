'''
Let's define f(x) as the number of times at which the integer x can be divided by 2.
You are given N numbers, and you should print the maximum f(x) among all these numbers.

Input
The first line contains one number N (1≤N≤105).
The second line contains N space-separated numbers where each number is between 1 and 1018 (inclusive).

Output
Print the maximum f(x) among all numbers.
'''
x = input()
n = list(map(int,input().split()))
def log2(num):
    n = 0
    while num % 2 ==0:
        n +=1
        num //=2
    return n
print(max(list(map(log2,n))))
