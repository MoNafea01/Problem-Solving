'''
Given a number X. Determine if the number is prime or not
Note:
A prime number is a number that is greater than 1 and has only two factors which are 1 and itself.
In other words : prime number divisible only by 1 and itself.
Be careful that 1 is not prime .
The first few prime numbers are

Input
Only one line containing a number X (2≤X≤105).

Output
print "YES" if the number is prime and "NO" otherwise.
'''
def prime(n):
    if n==0 or n==1:
        return 'NO'
    for i in range(2,n):
        if n%i==0:
            return 'NO'
    return 'YES'
print(prime(int(input())))
