'''
Given a number X. Determine in which of the following intervals the number X belongs to:
[0,25], (25,50], (50,75], (75,100]
Note:
if X belongs to any of the above intervals print "Interval " followed by the interval.
if X does not belong to any of the above intervals print "Out of Intervals".
The symbol '(' represents greater than.
The symbol ')' represents smaller than.
The symbol '[' represents greater than or equal.
The symbol ']' represents smaller than or equal.
For example:
[0,25] indicates numbers between 0 and 25.0000, including both.
(25,50] indicates numbers greater than 25: (25.00001) up to 50.0000000.

Input
Only one line containing a number X ( - 1000 ≤ X ≤ 1000).

Output
Print the answer to the problem above.
'''
i,j,k,l = ['[0,25]', '(25,50]', '(50,75]', '(75,100]']
x = float(input())
if x<=25 and x>=0:
    print('Interval',i)
elif x<=50 and x>25:
    print('Interval',j)
elif x<=75 and x >50:
    print('Interval',k)
elif x<=100 and x >75:
    print('Interval',l)
else:
    print('Out of Intervals')
