'''
Given a number N. Print the result of doing the following operation on N:
Convert N to its binary representation.
Count number of ones in the above binary representation.
Print the equivalent decimal number that its binary representation has only the number of ones that were counted above.
For example: (10)decimal = (1010)binary has 2 ones "11", after converting "11" to decimal number it will become 3.

Input
First line contains a number T (1≤T≤10) number of test cases.
Next T lines will contain a number N (1≤N≤231-1).

Output
For each test case print a single line contains the answer according to the required above.
'''
def binary_list(n): # to make the number represented as binary e.g. 10 is represented like [1,0,1,0]
    lst=[]
    inp = n
    while inp:
        if inp%2 == 0:
            lst.append(0)
            inp //= 2
        else:
            lst.append(1)
            inp //= 2
    lst.reverse()
    return lst
def binary_ones(n): # that function takes a list and make a new list of ones from it e.g. 10 => 1 0 1 0 => [1,1]
    counter = n.count(1)
    lst = []
    for i in range(counter):
        lst.append(1)
    return lst
def repr_ones(n): # this function takes the ones_list and represents it as decimal again [1,1] => 3
    c,a = 0,0
    for i in range(len(n)):
        c += 2**a
        a+=1
    return c
inp = int(input())
for i in range(inp):
    x = int(input())
    b_list = binary_list(x)
    ones_list = binary_ones(b_list)
    print(repr_ones(ones_list))
