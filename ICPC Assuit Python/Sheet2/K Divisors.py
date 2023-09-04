'''
Given a number N. Print all the divisors of N in ascending order.

Input
Only one line containing a number N(2≤N≤104).

Output
Print all positive divisors of N, one number per line.
'''
def divisor(n):
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    return lst
lst = divisor(int(input()))
print(*lst,sep='\n')
