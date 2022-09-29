list1=[7,2,4,8,3,9]

for i in range(len(list1)//2):
    list1[i],list1[len(list1)-i-1]=list1[len(list1)-i-1],list1[i]

print(list1)
