list1=[10,20,20,30,30,40,50]
def foo():
    pivot=0
    temp=[0]*len(list1)
    for index in range(len(list1)-1):
        if list1[index]!=list1[index+1]:
            temp[pivot]=list1[index]
            pivot+=1

    temp[pivot]=list1[-1]
    for item in temp:
        if temp.count(0)>0:
            temp.remove(0)
    return temp

print(foo())

list2=[0]*5

print(list2)