# list1=[1,2,2,3,4,4,4,5,5]

# def foo(list1):
#     temp=[0]*len(list1)
#     pivot=0
#     for ele in range(len(list1)-1):
#         if list1[ele]!=list1[ele+1]:
#             temp[pivot]=list1[ele]
#             pivot+=1
#     temp[pivot]=list1[-1]
#     return temp[:pivot+1]

# print(foo(list1))

#finding the gcd of two element 
# def foo(num1,num2):
#     if num1%i == 0:
#         return 
#     else:
#         if 

str1="prateek"
dict2={}
# for ele in str1:
#     if ele not in dict2:
#         dict2[ele]=1
#     else:
#         dict2[ele]+=1
# print(dict2)
dict1={x:((dict2.get(x,0)+1) if x in dict2 else 1) for x in str1}
print(dict1)