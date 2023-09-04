'''
Given a mathematical expression. The expression will be one of the following expressions: A+B, A−B, A∗B and A/B.
Print the result of the mathematical expression.

Input
Only one line contains A,S and B ( 1 ≤ A , B ≤ 104 ) , S is either ( + , − , ∗ , / ).

Output
Print the result of the mathematical expression.
'''
st = input()
if len(st.split('+')) == 2:
    st = st.split('+')
    print(int(st[0])+int(st[1]))
elif len(st.split('-')) == 2:
    st = st.split('-')
    print(int(st[0])-int(st[1]))
elif len(st.split('*')) == 2:
    st = st.split('*')
    print(int(st[0])*int(st[1]))
elif len(st.split('/')) == 2:
    st = st.split('/')
    print(int(st[0])//int(st[1]))
