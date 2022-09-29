list1=[10,20,30,40,50,40,20,30,70,60]

result=None
def foo(list1):
    global result
    if len(list1)==1:
        return list1[0] if list1[0]>=result else result
    else:
        if list1[0]>list1[1]:
            result=list1[0]
        else:
            result=list1[1]
    return foo(list1[1:])

            

print(foo(list1))