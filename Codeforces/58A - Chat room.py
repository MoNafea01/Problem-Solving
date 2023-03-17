def chat():
    t="hello"
    x=0
    s=input()
    for i in range(len(s)):
        if s[i] == t[x]:
            x+=1
        if x==5:
            return "YES"
    return "NO"
print(chat())
