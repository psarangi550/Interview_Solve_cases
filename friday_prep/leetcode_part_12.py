list1=[8,1,2,2,3]
# print(list1)
def foo(list1):
    temp=list1
    list2=sorted(list1,reverse=True)
    count=0
    result={}
    for i in range(len(list2)-1):
        if list2[i]==list2[i+1]:
            continue
        else:
            count=len(list2[i+1:])
        result[list2[i]]=count
    result[list2[-1]]=0
    print(result)
    print([f"{temp[i]}-->{result[temp[i]]}" for i in range(len(temp)-1) if temp[i]!=temp[i+1]]+[f'{temp[-1]}-->{result[temp[-1]]}'])
    return [result[temp[i]] for i in range(len(temp)-1)]+[result[temp[-1]]]


print(foo(list1))
    

