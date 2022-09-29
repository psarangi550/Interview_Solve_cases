tup1=(("a",23),("b",37),("c",11),("d",29))
list1=[]

# def bar(tup1):
#     min_val=tup1[0]
#     for ele in tup1:
#         if ele[0]<min_val[0]:
#             min_val=ele
#     return min_val

# def bar1(tup1):
#     min_val=tup1[0]
#     for ele in tup1:
#         if ele[1]>min_val[1]:
#             min_val=ele
#     return min_val


# temp=tup1
# def foo(tup1):
#     global list1
#     if (len(tup1)==1):
#         min_val=bar(temp)
#         list1.insert(0,min_val)
#         return tuple(list1)
#     else:
#         if tup1[0]>tup1[1]:
#             if tup1[0] not in list1:
#                 list1.append(tup1[0])
#         else:
#             if tup1[1] not in list1:
#                 list1.append(tup1[1])
#     return foo(tup1[1:])
# print(foo(tup1))


def bar1(tup1):
    mx_val=tup1[0]
    for ele in tup1:
        if ele[1]>mx_val[1]:
            max_val=ele
    return max_val

print(bar1(tup1))

temp=tup1
def foo1(tup1):
    global list1
    if (len(tup1)==1):
        max_val=bar1(temp)
        list1.insert(0,max_val)
        return tuple(list1)
    else:
        if tup1[0][1]<tup1[1][1]:
            if tup1[0] not in list1:
                list1.append(tup1[0])
        else:
            if tup1[1] not in list1:
                list1.append(tup1[1])
    return foo1(tup1[1:])
print(foo1(tup1))

# tup1=list(tup1)
# for i in range(len(tup1)):
#     for j in range(len(tup1)-i-1):
#         if tup1[j]>tup1[j+1]:
#             max=tup1[j]
#             tup1[j] = tup1[j+1]
#             tup1[j+1] =max
# print(tup1)