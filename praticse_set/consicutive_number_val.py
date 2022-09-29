list1=[1,1,0,1,1,1]

result=[]

def func(list1):
    global result
    if len(list1)==1:
        result.append(1) if list1[0]==1 else 0
        return result 
    else:
        if list1[0]==1:
            return 1+func(list1[1:]) 
        else:
            return 0+func(list1[1:])

func(list1)
print(result)
