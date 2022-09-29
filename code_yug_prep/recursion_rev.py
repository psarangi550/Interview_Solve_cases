list1=[1,2,3,1,1,2,3,4,4,1,2,3,1,2,3,1,2]

# count=0
def foo(list1):
    if len(list1)==1:
        return 1 if list1[0]==1 else 0
    else:
        if list1[0]==1:
            return 1+foo(list1[1:])
        else:
            return 0+foo(list1[1:])

# print(foo(list1))    

#counting the max and min values using the recursion as 

def bar(list1):
    if len(list1)==1:
        return list1[0]
    else:
        return max(list1[0],bar(list1[1:]))

# print(bar(list1))

def bar2(list1):
    if len(list1)==1:
        return list1[0]
    else:
        return min(list1[0],bar(list1[1:]))

print(bar2(list1))
