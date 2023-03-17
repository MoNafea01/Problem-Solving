def merge_the_tools(string, k):
    list2=[]
    m=k
    str1=""
    for n in range(0,len(string)+1,m):
        list1=string[n:m]
        m+=k
        for i in list1:
            if i not in list2:
                list2.append(i)
        for e in list2:
            str1+=e
        print(str1)
        str1=""
        list2.clear()
