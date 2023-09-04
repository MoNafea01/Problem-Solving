'''
Given two numbers X, Y which donate coordinates of a point in 2D plan. Determine in which quarter does it belong.
Note:
Print Q1, Q2, Q3, Q4 according to the quarter in which the point belongs to.
Print "Origem" If the point is at the origin.
Print "Eixo X" If the point is over X axis.
Print "Eixo Y" if the point is over Y axis.

Input
Only one line containing two numbers X, Y ( - 1000 ≤ X, Y ≤ 1000).

Output
Print the answer to problem above.
'''
c1,c2 = list(map(float,input().split()))
if c1>0 and c2>0:
    print('Q1')
elif c1<0 and c2>0:
    print('Q2')
elif c1<0 and c2<0:
    print('Q3')
elif c1>0 and c2<0:
    print('Q4')
elif c1==0 and c2 == 0:
    print('Origem')
elif c1==0:
    print('Eixo Y')
else:
    print('Eixo X')
