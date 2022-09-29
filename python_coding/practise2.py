list1=[2,4,6,8,10,12]
list2=[3,6,9,12,15,18]

dict1={}

for ele in list1:
    if ele not in dict1:
        dict1[ele]=1
    else:
        dict1[ele]+=1

for ele in list2:
    if ele in dict1:
        print(ele,end=" ")
    else:
        continue



