'''
Given three numbers n , k and a. 
Identify whether the data type of (n * k / a) is int, long long or double.

Input
Only one line containing three numbers n , k and a ( 1 ≤ a , k , n ≤ 2147483647 ).

Output
Print "int", "long long" or "double" (without quotes) as described in the statement.
Note:
int Range: [−2147483648,2147483647].
'''
x,y,z = list(map(int,input().split()))
def dtype_comparator(x,y,z):
    n = (x*y)/z
    if str(n).__contains__('e'):
        return 'long long'
    str_n = str(n).split('.')
    if str_n[1] == '0':
        if int(str_n[0]) > 2147483648:
            return 'long long'
        return 'int'
    return 'double'
print(dtype_comparator(x,y,z))
