list1=[8,1,2,2,3]
output=[4,0,1,1,3]
result=[]
for i in range(len(list1)):
    count=0
    temp=list1.copy()
    temp.remove(list1[i])
    for j in range(len(temp)):
        print(temp,list1[i])
        print(f"{list1[i]}>={temp[j]}")
        if list1[i]>temp[j]:
            count+=1
    result.append(count)

print(result)
