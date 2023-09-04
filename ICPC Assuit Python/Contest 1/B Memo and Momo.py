'''
Memo and Momo are playing a game. Memo will choose a positive number a , and Momo will choose a positive number b.
Your task is to tell them who will win according to the following rules:
If both a and b are divisible by k, 
both of them win and you should print "Both".
If a is divisible by k but b isn't,
Memo wins and you should print "Memo".
If b is divisible by k but a isn't,
Momo wins and you should print "Momo".
If both a and b are not divisible by k,
no one wins and you should print "No One".

Input
Only one line containing three positive numbers a , b and k ( 1 ≤ a , b , k ≤ 1018 ).

Output
Print the answer as described in the statement.
'''
x,y,z = list(map(int,input().split()))
def Memo_Momo(x,y,z):
    if le(x,z) == 0 and le(y,z) == 0:
        return 'Both'
    elif le(x,z) == 0:
        return 'Memo'
    elif le(y,z) == 0:
        return 'Momo'
    return 'No One'
def le(x,y):
    z = str(x/y).split('.')
    if z[1]=='0':
        return 0
    return 1
print(Memo_Momo(x,y,z))
