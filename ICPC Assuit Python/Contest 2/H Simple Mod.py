'''
Some day, an artist wanted to draw an X mark on the wall in a fashionable way.
He wanted to do so by grouping snippets of slashes /, backslashes \, asterisks * and a capital X letter in an N×N 
square as shown in the sample. Can you help him?

Input
Only one line containing one odd number N (3≤N≤49).

Output
Print the fashionable drawing.
'''
x = int(input())
for i in range(x):
    for j in range(x):
        if i==j and i != x//2 and j != x//2:
            print('\\',end='')
        elif i == x//2 and j == x//2:
            print('X',end='')
        elif (j != x//2 and x-1-j==i):
            print('/',end='')
        else:
            print('*',end='')
    print()
    