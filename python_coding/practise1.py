list1=[10,20,30,20,40,30,50]

def foo(list1):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]>list1[j]:
                list1[i],list1[j]=list1[j],list1[i]    
    return list1

print(foo(list1))