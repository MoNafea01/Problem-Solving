'''
You are given N numbers, and you should divide them into consecutive groups of size K, then print the minimum among each group.
If the last group is of size <K, print the minimum number found just after the last number received.
For more explanation, see the notes.

Input
First line contains two numbers N,K(1≤K≤N≤105) – the number of values, and the range length after which you should print the minimum.
Second line contains N numbers (−109≤x≤109).

Output
Print the answer in a single line.
'''
N,K = list(map(int,input().split()))
lst = list(map(int,input().split()))
i=0
lst2 = []
if K > 1:
    while i < len(lst):
        lst2.append(lst[i:i+K])
        i+=K
    lst2 = list(map(min,lst2))
    print(*lst2)
else:
    print(*lst)