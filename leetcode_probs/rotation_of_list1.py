list1=[1,2,3,4,5]

def foo(list1,k):
    count=0
    val=list1+list1
    for i in range(len(list1)):
        for j in range(len(list1)):
            if count<k:
                print(val[i+j],end="")
            else:
                break
        count+=1
        print()
        

foo(list1,3)