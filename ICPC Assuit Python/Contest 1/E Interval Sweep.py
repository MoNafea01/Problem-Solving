'''
Given two numbers a and b. You have to answer with "YES" if there is a non-empty interval consisting of numbers from l to r ( l , l+1 , l+2 , ... , r)
with a odd numbers and b even numbers, or "NO" otherwise.

Input
Only one line containing two numbers a and b ( 0 ≤ a , b ≤ 100)
the number of odd numbers and the number of even numbers in the interval respectively.

Output
Print "YES" or "NO" as described in the statement.
'''
x,y = input().split()
x,y=int(x),int(y)
if x==0 and y==0:
    print('NO')
elif abs(x-y) <=1:
    print('YES')
else:
    print('NO')
