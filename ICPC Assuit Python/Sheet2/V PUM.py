'''
Given a number N. Print N lines that describes PUM game.
For more clarification see the examples.

Input
Only one line containing a number N (1≤N≤20).

Output
Print the answer according to the required above.
'''
x = int(input())
c = 1
for i in range(x*4):
    if c%4 ==0 :
        print('PUM')
        c+=1
        continue
    print(c,end=' ')
    c+=1
