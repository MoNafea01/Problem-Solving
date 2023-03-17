num=int(input())
list1=[]
count1=0
count2=0
for i in range(num):
    list1.append([int(x) for x in input().split()])
for i in list1:
    for j in i:
        if int(j==1):
            count1+=1
    if count1>=2:
        count2+=1
    count1=0
print(count2)
