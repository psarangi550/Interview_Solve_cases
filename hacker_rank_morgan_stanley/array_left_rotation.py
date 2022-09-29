def foo(list1,num):
    for i in range(num):
        result=[]
        temp=list1[:num]
        for j in range(num,len(list1)):
            result.append(list1[j])
        result.extend(temp)
    return result

def bar(list1,num):
    for i in range(num):
        temp=list1[0]
        for j in range(0,len(list1)-1):
            list1[j]=list1[j+1]
        list1[-1]=temp
    return list1

print(foo([1,2,3,4,5,6,7],3))
print(bar([1,2,3,4,5,6,7],3))


    
