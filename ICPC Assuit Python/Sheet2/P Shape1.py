'''
Given a number N. Print a face down right angled triangle that has N rows.
For more clarification see the example below.

Input
Only one line containing a number N (1≤N≤99).

Output
Print the answer according to the required above.
'''
x = int(input())
for i in range(x,0,-1):
    print('*'*i)
