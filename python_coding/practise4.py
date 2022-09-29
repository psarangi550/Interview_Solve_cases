list1=[2,17,6,8,1]


result=[]

for i in range(len(list1)-1):
    if list1[i]>=list1[i+1]:
        result.append(list1[i])
    else:
        continue
result.append(list1[len(list1)-1])

print(result)
