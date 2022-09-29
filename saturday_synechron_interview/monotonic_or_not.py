# from time import monotonic
list1 = [6, 5, 4, 4]
list2 = [1,1,1,3,3,4,3,2,4,2]
list3 = [1,1,2,3,7]


def foo(list1):
    result=[]
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]<=list1[j]:
                result.append("monotonic")
            else:
                result.append("not monotonic")
    for ele in result:
        if ele !="monotonic":
            return False
            break
        else:
            continue
    return True
            


print(foo(list2))
print(foo(list3))

