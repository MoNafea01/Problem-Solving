n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())
for i in list1:
    if len(i) <=10:
        list2.append(i)
    else:
        i=i[0]+str(len(i)-2)+i[len(i)-1]
        list2.append(i)
for i in list2:
    print(i)