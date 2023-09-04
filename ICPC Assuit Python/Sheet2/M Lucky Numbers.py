'''
Given two numbers A and B. Print all lucky numbers between A and B inclusive.
Note:
The Lucky number is any positive number that its decimal representation contains only 4 and 7.
For example: numbers 4, 7, 47 and 744 are lucky and numbers 5, 17 and 174 are not.

Input
Only one line containing two numbers A and B (1≤A≤B≤105).

Output
Print all lucky numbers between A and B inclusive separated by a space. If there is no lucky number print -1.
'''
A,B = map(int,input().split())
def lucky(A,B):
    lst=[]
    for i in range(A,B+1):
        x = str(i)
        c = 0
        for j in x:
            if int(j) == 4 or int(j) ==7:
                c+=1
        if c == len(x):
            lst.append(x)
            print(x,end=' ')
    return -1 if len(lst)==0 else ''
print(lucky(A,B))
