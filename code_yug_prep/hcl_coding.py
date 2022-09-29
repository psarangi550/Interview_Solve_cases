from functools import reduce
list1=[1,2,3,4]

def foo(list1):
    result=[]
    for index,ele in enumerate(list1):
        temp=[1,2,3,4]
        temp.remove(ele)
        val=reduce(lambda x,y:x*y,temp)
        result.append(val)
    return result

print(foo(list1))


