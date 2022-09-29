import heapq

list1=[10,20,30,40,30,30]

# list2=list(set(list1))

# print(list2)

# print(heapq.nlargest(3,list2)[-1])

list2=[]

for ele in list1:
    if ele not in list2:
        list2.append(ele)
print(list2)

def bar(list1,n):
    temp=list1
    for i in range(n-1):
        temp.remove(max(temp))
    return temp[-1]
print(bar(list2,2))
