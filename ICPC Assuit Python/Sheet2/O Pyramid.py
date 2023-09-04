'''
Given a number N. Print a left angled triangle that has N rows.
For more clarification see the example below.

Input
Only one line containing a number N (1≤N≤99).

Output
Print the answer according to the required above.
'''
x = int(input())
for i in range(1,x+1):
    print('*'*i)
