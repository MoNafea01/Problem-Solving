'''
Hady wants to ride a train. He knows his seat number, but he doesn't know the corresponding row or column number of his seat. However, he knows that each row consists of exactly 4
seats. The train seats are numbered from zero as shown in the figure:

Input
Only one line containing id (0≤id≤1018) – the seat number.

Output
The row and column numbers of the seat.

'''
id_ = int(input())
row = id_ // 4
col=0
if row%2==1:
    if (id_ - 1) % 4 == 0:
        col = 2
    elif (id_ - 2)%4 == 0:
        col = 1
    elif (id_ - 3)%4 == 0:
        col = 0
    else:
        col = 3
else:
    if (id_ +1) % 4 == 0:
        col = 3
    elif(id_+2) % 4 == 0:
        col = 2
    elif(id_+3)%4 ==0:
        col = 1
    else:
        col = 0
print(f"{row} {col}")