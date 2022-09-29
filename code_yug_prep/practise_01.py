list1=[0,3,1,4,3,7,6,9,12]
def foo(list1):
    a=list1[0]
    b=list1[1]
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]*list1[j]>(a*b):
                a=list1[i]
                b=list1[j]
    return a,b

print(foo(list1))