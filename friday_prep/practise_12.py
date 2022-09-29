list1=[["B","C"],["D","B"],["C","A"]]
# list1=[["London","NewYork"],["NewYork","Lima"],["Lima","Sao polo"]]
# def foo(list1):
#     result=[]
#     for ele in list1:
#         for index,item in enumerate(ele):
#             if index%2==0:
#                 result.append(item)
#     return result

# def bar(list1):
#     val=foo(list1)
#     for ele in list1:
#         if ele[1] not in val:
#             print(ele[1])

# bar(list1)


def foo(list1):
    return map(set,zip(*list1))

for item in foo(list1):
    print(item)