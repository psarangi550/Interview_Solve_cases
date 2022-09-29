# def foo(str1,str2):
#     s1=set(str1)
#     s2=set(str2)
#     return s1&s2

# print(foo("naina","reene"))


list1=[5,32,45,4,12,18,25]

def foo(list1):
    list1.sort()
    max_diff=-999999
    for i in range(len(list1)-1):
        if list1[i+1]-list1[i]>max_diff:
            max_diff=list1[i+1]-list1[i]
    return max_diff

def bar(list1):
    list1.sort()
    min_diff=999999
    for i in range(len(list1)-1):
        if list1[i+1]-list1[i]<min_diff:
            min_diff=list1[i+1]-list1[i]
    return min_diff


print(foo(list1))
print(bar(list1))