list1=[10,20,20,30,30,40]



def foo(list1):
    temp=[0]*len(list1)
    pivot=0
    for ele in range(0,len(list1)-1):
        if list1[ele]!=list1[ele+1]:
            temp[pivot]=list1[ele]
            pivot+=1
        temp[pivot]=list1[len(list1)-1]
    return temp[pivot]

# print(temp)
print(foo(list1))

