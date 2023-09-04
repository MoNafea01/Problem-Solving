'''
The Egyptian football team will be in Russia for the World Cup. Of course, they all would like to buy souvenirs for their families.
Luckily, they met the king of souvenirs Matryoshka who is famous for his masterpiece Katryoshka. He makes it using different wooden pieces:
eyes, mouths and bodies. He can form a nice Katryoshka using one of the following combinations:
-Two eyes and one body.
-Two eyes, one mouth, and one body.
-One eye, one mouth, and one body.
If the king has n eyes, m mouths and k bodies,
what is the largest number of Katryoshkas he can make?

Input
Only one line containing three numbers n , m and k(0≤n,m,k≤1018) – the number of eyes, mouths and bodies respectively.

Output
Print the largest number of Katryoshkas he can make.
'''
def Katryoshka(n,m,k):
    if n == 0 or k == 0:
        return 0
    if m == 0 :
        if n < k :
            return n // 2
        else:
            return min(n//2,k)
    if k < m and k < n:
        return k
    if n < k and n < m :
        return n
    kat = 0
    if m < n and m < k:
        kat += m
        n -= m
        k -= m
        if n < k:
            kat += n//2
        else:
            kat += min(n//2,k)
    return kat
m,n,k = list(map(int,input().split()))
print(Katryoshka(m,n,k))
