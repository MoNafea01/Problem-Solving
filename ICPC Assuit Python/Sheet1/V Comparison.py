'''
Given a comparison symbol S between two numbers A and B. Determine whether it is Right or Wrong.
The comparison is as follows: A < B, A > B, A = B.
Where A, B are two integer numbers and S refers to the sign between them.

Input
Only one line containing A, S and B respectively (-100  ≤  A, B  ≤  100), S can be ('<', '>','=') without the quotes.

Output
Print "Right" if the comparison is true, "Wrong" otherwise.
'''
x,op,y = input().split()
x,y = int(x),int(y)
if op == '>' and x>y:
    print('Right')
elif op == '<' and x<y:
    print('Right')
elif op == '=' and x==y:
    print('Right')
else:
    print('Wrong')
