from itertools import count


list1=[-1,150,190,170,-1,-1,160,180]


result=[]
for ele in list1:
    if ele !=-1:
        result.append(ele)

result.sort()
count=0
for ele in range(len(list1)):
    if list1[ele] ==-1:
        continue
    else:
        list1[ele]=result[count]
    count+=1

print(list1)
