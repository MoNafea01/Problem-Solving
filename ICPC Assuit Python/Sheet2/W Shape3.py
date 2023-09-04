'''
Given a number N. Print N lines that describes PUM game.
For more clarification see the examples.

Input
Only one line containing a number N (1≤N≤20).

Output
Print the answer according to the required above.
'''
n = int(input())
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
print('*' * (2*n - 1))
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        print('*', end='')
    print()
