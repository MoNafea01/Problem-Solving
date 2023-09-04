'''
Given a number N. Print all prime numbers between 1 and N inclusive.
A prime number is a number that is greater than 1 and has only two factors which are 1 and itself.
In other words : prime number divisible only by 1 and itself.
Be careful that 1 is not prime .
The first few prime numbers are

Input
Only one line containing a number N(2≤N≤103).

Output
Print all prime numbers between 1 and N(inclusive) separated by a space.
'''
x = int(input()) + 1
counter = 0
lst=[]
def prime(n):
    if n==0 or n==1:
        return 0
    if n==2:
        return 1
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
while True:
    if counter == x:
        break
    if prime(counter) == 1:
        lst.append(counter)
    counter +=1
for i in lst:
    if i==lst[-1]:
        print(i)
    else:
        print(i,end=' ')
