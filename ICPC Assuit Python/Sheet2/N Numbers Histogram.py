'''
Given 3 lines of input described as follow:
First line contains a symbol Sز
Second line contains a number N.
Third line contains N numbers.
For each number Xi in the N numbers print a new line that contains the symbol S repeated Xi time.

Input
The first line contains a symbol S can be (+,- ,* ,/ ).
The second line an number N (1≤N≤50).
The third line contains N numbers (1≤Xi≤100).

Output
Print the answer required above.
'''
S = input()
n1 = input()
lst = list(map(int,input().split()))
for i in lst:
    print(S*i)
