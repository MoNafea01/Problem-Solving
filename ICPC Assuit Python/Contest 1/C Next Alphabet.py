'''
Given a lowercase alphabet character. You have to print the next character in the alphabet.

Input
Only one line containing a lowercase English letter C.

Output
Print the next letter to C in the alphabet.
Note
The next letter to z is a.
'''
x=input()
y=ord(x)
asc=chr(y)
if asc == 'z':
    print('a')
else:
    asc=chr(y+1)
    print(asc)
