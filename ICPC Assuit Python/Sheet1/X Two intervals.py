'''
Given the boundaries of 2 intervals. Print the boundaries of their intersection.

Note: Boundaries mean the two ends of an interval which are the starting number and the ending number.

Input
Only one line contains two intervals [l1,r1] , [ l2 , r2 ] where ( 1 ≤ l1 , l2 , r1 , r2 ≤ 109 ) , (l1≤r1,l2≤r2).
It's guaranteed that l1≤r1
 and l2≤r2.

Output
If there is an intersection between these 2 intervals print its boundaries , otherwise print -1.
'''
l1,r1,l2,r2 = list(map(int,input().split()))
if l1 <= l2 and r1 >= r2:
    print(l2,r2)
    
elif l2 <= l1 and r2 >= r1:
    print(l1,r1)
    
elif l1 <= l2 and r1 >= l2:
    print(l2,r1)
elif l2 <= r1 and r2 >= l1:
    print(l1,r2)
    
elif l1 < l2 and r1 == l2:
    print(l2)
elif l2 < l1 and r2 == l1:
    print(r2)
else:
    print(-1)
