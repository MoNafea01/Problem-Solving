'''
Given two numbers A and B. Print the greatest common divisor between (A,B).
Note: The greatest common divisor (GCD) of two or more integers, which are not all zeroes,
is the largest positive integer that divides each of the integers.
For example:
the GCD of 8 and 12 is 4.
because the numbers that divides both 8 and 12 are (1,2,4) and 4 is the largest one .

Input
Only one line containing two numbers A and B (1≤A,B≤103).

Output
Print the GCD of A and B.
'''
A,B = map(int,input().split())
def divisor(n):
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    return lst
l1,l2 =divisor(A),divisor(B)
lst=[]
for i in l1:
    if i in l2:
        lst.append(i)
print(lst[-1])
