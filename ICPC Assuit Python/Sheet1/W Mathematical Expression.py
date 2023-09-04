'''
Given a mathematical expression. The expression will be one of the following expressions:
A + B = C, A - B = C and A * B = C
where A, B, C are three numbers, S is the sign between A and B, and Q the '=' sign
Print "Yes" If the expression is Right , Otherwise print the right answer of the expression.

Input
Only one line containing the expression: A, S, B, Q, C respectively (0 ≤ A, B ≤ 100,  - 105 ≤ C ≤ 105) and S can be ('+', '-', '*') without the quotation.

Output
Output either "Yes" (without the quotation) or the right answer depending on the statement.
'''
lst = input().split()
x = float(lst[0])
op = lst[1]
y = float(lst[2])
res = float(lst[4])
if op == '+' and x+y==res:
    print('Yes')
elif op == '-' and x-y==res:
    print('Yes')
elif op == '*' and x*y == res:
    print('Yes')
elif op=='/' and x/y==res:
    print('Yes')
elif op == '+':
    print(int(x+y))
elif op == '-':
    print(int(x-y))
elif op == '*':
    print(int(x*y))
else:
    print(int(x/y))
