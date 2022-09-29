# list1=[3,2,5,8,1,7]

# def foo(list1):
#     output=[]
#     for i in range(len(list1)-1):
#         result=[list1[i],list1[i+1]]
#         output.append(result)
#     return output

# print(foo(list1))


# list1=[1,1,2,2,3,4,5,6]

# def foo(list1):
#     temp=[0]*len(list1)
#     pivot=0
#     for i in range(len(list1)-1):
#         if list1[i]!=list1[i+1]:
#             temp[pivot] = list1[i]
#             pivot+=1
#         else:
#             continue
#     temp[pivot]=list1[-1]
#     return temp[:pivot+1]

# print(foo(list1))