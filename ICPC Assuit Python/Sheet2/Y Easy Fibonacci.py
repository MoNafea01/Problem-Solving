'''
Given a number N. Print first N numbers of the Fibonacci sequence.
Note: In order to create the Fibonacci sequence use the following function:
fib(1) = 0.
fib(2) = 1.
fib(n) = fib(n - 1) + fib(n - 2).

Input
Only one line containing a number N (1≤N≤45).

Output
Print the first N numbers from the Fibonacci Sequence .
'''
n= int(input())
def fib(n):
    f1 = 0
    f2 = 1
    if (n < 1):
        return
    print(f1, end=" ")
    for x in range(1, n):
        print(f2, end=" ")
        next = f1 + f2
        f1 = f2
        f2 = next
fib(n)
