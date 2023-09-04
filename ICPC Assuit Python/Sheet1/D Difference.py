'''
Given four numbers A, B, C and D. Print the result of the following equation :
 X = (A * B) - (C * D).

Input
Only one line containing 4 separated numbers A, B, C and D ( - 105  ≤  A, B, C, D  ≤  105).

Output
Print "Difference  =  " without quotes followed by the equation result.
'''
x = list(map(int,input().split()))
print(f"Difference = {x[0]*x[1]-x[2]*x[3]}")
