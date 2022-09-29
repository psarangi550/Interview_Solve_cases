list1=[2,0,2,3,0,5,4,5,0,3,1,0,0,1,1,2,3,1]

def foo(list1):
    if len(list1)==1:
        return 1 if list1[0]==1 else 0
    else:
        if list1[0]==1:
            return 1+ foo(list1[1:])
        if list1[0]!=1:
            return 0 + foo(list1[1:])

print(foo(list1))
    
