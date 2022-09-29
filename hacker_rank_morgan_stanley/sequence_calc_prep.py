list1=[5,2,1,3,4]
list2=[2,3,1]

def foo(list1):
    result=[]
    for i in range(1,len(list1)):
        if i in list1:
            total_index=list1.index(i)+1
            if total_index in list1:
                final=list1.index(total_index)+1
                result.append(final)
    last_index=list1.index(list1.index(i+1)+1)+1
    result.append(last_index)
    return result


print(foo(list1))
print(foo(list2))


