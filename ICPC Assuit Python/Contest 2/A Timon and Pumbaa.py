'''
Timon has a candies and his friend, Pumbaa, has b candies, 
so Pumbaa asked Timon to tell him the value of a−b. However, Timon will tell him the value of a−b if the value is ≥0; otherwise, 
he will lie and say 0. Since it was a hard task for Timon, he's asking for your help.
Given two numbers a and b, find the answer.

Input
Only one line containing two numbers a,b (1≤a,b≤109).

Output
Print the answer as specified in the statement.
'''
a,b = map(int,input().split())
if (a-b)>=0:
    print(a-b)
else:
    print(0)
