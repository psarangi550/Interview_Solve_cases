input=[3,2,1,5,4,2]


def bar(list1):
    result=[]
    for ele in list1:
        if ele not in result:
            result.append(ele)
    return result

val=bar(input)
print(val)

def foo(list1):
    output=[]
    for i in range(len(list1)):#3
        for j in range(i+1,len(list1)):#212
            if list1[j]<list1[i]:
                list1[i],list1[j]=list1[j],list1[i]
    return list1

print(foo(val))