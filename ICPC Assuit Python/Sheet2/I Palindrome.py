'''
Given a number N. Print 2 lines that contain the following respectively:
Print N in a reversed order and not leading zeroes.
If N is a palindrome number print "YES" otherwise, print "NO.
Note:
A palindrome number is a number that reads the same forward or backward.
For example: 12321, 101 are palindrome numbers, while 1201, 221 are not.
A leading zero is any 0 digit that comes before the first nonzero digit in a number for example :
numbers (005 , 01 , 0123 , 02 , 000250 ) are leading zeroes but ( 5 , 123 , 20 ,2500 ) not leading zeroes numbers .

Input
Only one line containing a number N(1≤N≤107).

Output
Print the answer required above.
'''
x = list(map(int,list(input())))
y=list(reversed(x))
z=''.join(str(e) for e in y)
print(int(z))
if x==y:
    print('YES')
else:
    print('NO')
