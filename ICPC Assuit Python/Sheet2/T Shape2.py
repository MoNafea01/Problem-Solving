'''
Given a number N. Print a pyramid that has N rows.
For more clarification see the example below.

Input
Only one line containing a number N (1≤N≤99).

Output
Print the answer according to the required above.
'''
n = int(input())
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
