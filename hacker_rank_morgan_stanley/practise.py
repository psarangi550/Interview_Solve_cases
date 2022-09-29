def foo(list1):
    result=[]
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if j==1:
                result.extend([list1[-1],list1[0],list1[j]])
    return result

output=[]
k=0
def bar(list1,num):
    global output
    global k
    if k==num:
        return output
    else:
        output=foo(list1)
        k+=1
    return bar(output,num)

print(bar([3,4,5],1))