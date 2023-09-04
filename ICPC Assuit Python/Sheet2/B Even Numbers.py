'''
Given a number N. Print all even numbers between 1 and N inclusive in separate lines.

Input
Only one line containing a number N (1≤N≤103).

Output
Print the answer according to the required above. If there are no even numbers print -1.
'''
def print_even(n):
    if n==1 or n==0:
        print(-1)
        return
    for i in range(2,n+1,2):
        print(i)
print_even(int(input()))
