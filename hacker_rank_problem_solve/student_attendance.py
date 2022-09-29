def attendance(list1,thresold):
    count=0
    for ele in list1:
        if ele<=0:
            count+=1
    if thresold>count:
        print("YES")
    else:
        print("NO")

attendance([-1,-3,4,2],3)
attendance([0,-1,2,1],2)