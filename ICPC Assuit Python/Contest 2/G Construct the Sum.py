'''
You are given two integers n and s, and you have to find distinct positive integers, such that each of them is ≤n
, and their summation =s. Otherwise, state that this is impossible.

Input
The first line contains a number T (1≤T≤100) – number of test cases.
Each of the next T lines contains two space-separated integers n,s (1≤n≤105,1≤s≤1018).

Output
For each test case, if there is no possible answer, print -1 on a single line. Otherwise,
print the set of numbers that satisfy the above condition on a single line. You can print the numbers in any order.
If there are multiple answers, you can print any of them.
'''
x = int(input())
def construct_sum(n,s):
    m = [None] * n
    if (n*(n+1)//2 < s):
        return [-1]
    sum_ = 0
    counter = 0
    for i in range(n,1,-1):
        if (sum_ + i <= s):
            sum_ +=i
            m[counter] = i
            counter +=1
        if sum_ == s:
            break
    return m
while x:
    n,s = list(map(int,input().split()))
    z = construct_sum(n,s)
    z = filter(lambda a:a if a is not None else '',z)
    print(*z)
    x-=1
