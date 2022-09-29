list1=[5,32,45,7,12,18,25]

def bar(list1):
    list1=sorted(list1)
    size=len(list1)
    max_diff= -(999*999)
    for ele in range(size-1):
        if (list1[ele+1]-list1[ele])>max_diff:
            max_diff=(list1[ele+1]-list1[ele])
    return max_diff

print(bar(list1))