list1=[2,7,11,15]

left=0
right=len(list1)-1
sum_val=9

while left < right:
    if (list1[left]+list1[right])>sum_val:
        right-=1
    elif (list1[left]+list1[right])<sum_val:
        left+=1
    else:
        if (list1[left]+list1[right])==sum_val:
            print("positions are",left,right)
            right-=1
            left+=1



