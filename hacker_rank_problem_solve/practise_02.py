list1=[1,2,3,4,5,6]
k=5
out = []
for i in range(len(list1)):
    result =[]
    for j in range(i+1,len(list1)):
        if (list1[i]+list1[j])%k==0:
            result.append(list1[i])
            result.append(list1[j])
        else:
            continue
    if result:
        out.append(result)

print(out)