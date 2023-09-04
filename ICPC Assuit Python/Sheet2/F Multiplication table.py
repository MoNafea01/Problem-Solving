'''
Given a number N. Print the maltiplication table of the number from 1 to 12

Input
Only one line containing a number N (1≤N≤50).

Output
Print 12 lines according to the required above.
'''
x = int(input())
for i in range(1,13):
    print(f'{x} * {i} = {i*x}')
