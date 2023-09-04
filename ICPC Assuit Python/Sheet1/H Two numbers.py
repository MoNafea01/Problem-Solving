'''
Given 2 numbers A
and B
. Print floor, ceil and round of A/B
Note:
- Floor: Is a mathematical function that takes a real number X and its output is the greatest integer less than or equal to X
- Ceil: Is a mathematical function that takes a real number X and its output is the smallest integer larger than or equal to X
- Round: Is a mathematical function that takes a real number X and its output is the closest integer to that number X

Input
Only one line containing two numbers A and B ( 1 ≤ A , B ≤ 103 )

Output
Print 3 lines that contain the following in the same order:
"floor A / B = Floor result" without quotes.
"ceil A / B = Ceil result" without quotes.
"round A / B = Round result" without quotes.
'''
import math
x,y = list(map(int,input().split()))
def round_half_up(n):
    length_of_num = len(str(int(n)))+1
    if int(str(n)[length_of_num]) < 5:
        return round(n)
    return round(n+0.1)
print(f"floor {x} / {y} = {(x//y)}")
print(f"ceil {x} / {y} = {math.ceil(x/y)}")
print(f"round {x} / {y} = {round_half_up(x/y)}")
