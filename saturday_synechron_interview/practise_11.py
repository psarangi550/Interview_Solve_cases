list1=[0,1,0,3,12]
list2=[1,3,12,0,0]

temp=[]
count=0
for ele in list1:
    if ele==0:
        count=count+1
    else:
        temp.append(ele)
temp.extend([0 for i in range(count)])
print(temp)
