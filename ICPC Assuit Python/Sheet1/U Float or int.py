'''
Given a number N
Determine whether N is float number or integer number.
Note:
If N is float number then print "float" followed by the integer part followed by decimal part separated by space.
If N is integer number then print "int" followed by the integer part separated by space.

Input
Only one line containing a number N ( 1 ≤ N ≤ 103 )

Output
Print the answer required above.
'''
x,y = input().split('.')
leng = pow(10,len(y))
z = int(y)/leng
 
if int(y)==0:
    print('int',x)
else:
    print('float',x,z)
