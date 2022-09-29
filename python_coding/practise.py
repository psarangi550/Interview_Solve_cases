l1=[1,2,2,3,4,4,5,6]


def foo(l1):
    temp=[0]*len(l1)
    pivot=0
    for i in range(len(l1)-1):
        if l1[i]!=l1[i+1]:
            temp[pivot]=l1[i]
            pivot+=1
        temp[pivot]=l1[len(l1)-1]
    return temp[:pivot+1]

print(foo(l1))
