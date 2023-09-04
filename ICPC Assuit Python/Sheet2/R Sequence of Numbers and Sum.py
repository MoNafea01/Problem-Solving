'''
Given multiple lines each line contains two numbers N and M.
For each line print a single line contains:
The numbers between N and M inclusive separated by single space.
The message " sum =".
The summation of all numbers between N and M inclusive.
Note: The program should be TERMINATED as soon as any of these two numbers is less than or equal to zero and don't print any thing.
For more clarification see the examples below.

Input
The input contains multiple line.
Each line contains two numbers N and M (-100≤N,M≤100).
It's guaranteed that the last line of the input will contain a number that is less than or equal to zero.

Output
For each line print the answer according to the required above in a single line.
'''
while True:
    sum_ = 0
    x,y = input().split()
    x,y = int(x), int(y)
    min_,max_ = min(x,y),max(x,y)
    if min_ <=0:
        break
    for i in range(min_,max_+1):
        sum_ +=i
        print(i,end=' ')
    print(f'sum ={sum_}')
