def foo(total,list1):
    count=0
    d={}
    for ele in range(len(list1)):
        if list1[ele] not in d:
            d[list1[ele]]=0
        else:
            count+=1
            if count%2 == 0:
                d[list1[ele]]=count
            else:
               d[list1[ele]]=count//2 
    return total-sum(d.values())

# print(foo(9,[10,20,20,10,10,30,50,10,20]))
print(foo(7,[1,2,1,2,1,3,2]))
# foo(9,[10,20,20,10,10,30,50,10,20])
