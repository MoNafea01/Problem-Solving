'''
Given three numbers N,A,B. 
Print the summation of the numbers between 1 and N whose sum of digits is between A and B inclusive.

Input
Only one line containing three numbers N,A,B (1≤N≤104,1≤A≤B≤36).

Output
Print a single line contains the answer according to the required above.
'''
N,A,B = map(int,input().split())
def de_digit(lst):
    s = ''.join(str(e) for e in str(lst))
    return int(s)
def digit(n):
    line = list(str(n))
    line = list(map(int,line))
    return line
sum_ = 0
for i in range(A,N+1):
    line = digit(i)
    if sum(line) >= A and sum(line) <= B:
        x = de_digit(i)
        sum_ += int(x)
print(sum_)
