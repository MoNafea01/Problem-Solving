'''
Given 4 numbers A , B , C and D
. Print the last 2 digits from their Multiplication.

Input
Only one line containing four numbers A , B , C and D ( 2 ≤ A , B , C , D ≤ 109 ).

Output
Print the last 2 digits from their Multiplication.
'''
a,b,c,d = list(map(int,input().split()))
mul = a * b * c * d
print(str(mul)[-2:])
