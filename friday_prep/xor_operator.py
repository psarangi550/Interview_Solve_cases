def foo(list1):
    total_xor=0
    x_or=list1[0]
    final=0
    num=len(list1)
    for i in range(1,num+2):
        total_xor=total_xor^i
    for i in range(1,len(list1)):
        x_or=x_or^list1[i]
    final=total_xor^x_or
    return final

print(foo([1,2,3,5,6]))
