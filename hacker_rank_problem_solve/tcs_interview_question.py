# from operator impor
from functools import reduce

list1 = [1,2,3,4]
#output = [2*3*4=24,1*3*4=12,1*2*4=8,1*2*3=6]

list2=[]
mul=1
for index,ele in enumerate(list1):
    list1 = [1,2,3,4]
    list1.remove(ele)
    # print(list1)
    val=reduce(lambda x,y:x*y,list1)
    list2.append(val)

print(list2)
