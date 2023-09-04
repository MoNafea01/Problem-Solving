'''
Given 4 numbers A,B,C and D. If AB > CD
print "YES" otherwise, print "NO".

Input
Only one line containing 4 numbers A,B,C and D ( 1 ≤ A , C ≤ 107 ) , ( 1 ≤ B , D ≤ 1012 )

Output
Print "YES" or "NO" according to the problem above.
'''
import math
a,b,c,d = list(map(int,input().split()))
print('YES' if (b * math.log(a) > d * math.log(c)) else 'NO') 
# I Used log not the power because the power causes (Time limit exceeded) error
# log(a ^ b) = b * log (a)
