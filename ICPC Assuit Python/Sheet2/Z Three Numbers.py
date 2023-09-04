'''
Given two numbers K and S. Determine how many different values of X,Y and Z such that (0≤X,Y,Z≤K) and X+Y+Z=S.

Input
Only one line containing two numbers K and S (0≤K≤3000,0≤S≤3K).

Output
Print the answer required above.
'''
k,s = list(map(int,input().split()))
k,s = int(k),int(s)
c = 0
for i in range(0,k+1):
    for j in range(0,k+1):
        if (s-i-j >=0 and s-i-j <= k):
            c+=1
print(c)
