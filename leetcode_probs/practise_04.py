list1=[[1,2,3],[4,5,6],[7,8,9]]
result=[]
count=0
for n in range(len(list1)*2-1):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if i==j:
                print(list1[j][i])
                break
    break
    print()