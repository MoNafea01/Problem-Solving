'''
Given two numbers A and B. Print "Multiples" if A is multiple of B or vice versa. Otherwise print "No Multiples".

Input
Only one line containing two numbers A, B (1  ≤  A, B  ≤  106)

Output
Print the "Multiples" or "No Multiples" corresponding to the read numbers.
'''
x,y = list(map(int,input().split()))
if x%y == 0 :
    print('Multiples')
elif y%x == 0 :
    print('Multiples')
else:
    print('No Multiples')
  
