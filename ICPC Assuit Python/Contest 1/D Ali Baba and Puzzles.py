'''
One day, Ali Baba had an easy puzzle that he couldn't solve. The puzzle consisted of 4 numbers and his task was to check whether he could get the fourth number
using arithmetic operators (+,−,×) between the other three numbers; so that each operator is used only once.
a □ b □ c = d
Can you solve this tricky puzzle for him?

Input
Only one line containing four numbers a , b , c and d ( − 109 ≤ a , b , c ≤ 109 ) , ( −1018 ≤ d ≤ 1018 ).

Output
Print "YES" (without quotes) if you get the fourth number using arithmetic operators, otherwise, print "NO" (without quotes)
'''
import operator
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    }
def Ali_baba(x,y,z,res,ops):
    for i in ops:
        for j in ops:
            if i != j:
                n = ops[j](ops[i](x,y),z)
                if ops[j] == operator.mul:
                    n = ops[i](x,ops[j](z,y))
                if n==res:
                    return 'YES'
    return 'NO'
x,y,z,res = list(map(int,input().split()))
print(Ali_baba(x,y,z,res,ops))
