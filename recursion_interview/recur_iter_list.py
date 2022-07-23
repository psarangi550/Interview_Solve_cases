# list1=[2,0,1,3,4,0,0,1,5,3,2]

# def func(list1):
#     if len(list1)==1:
#         return 0 if list1[0] else 1
#     else:
#         if list1[0]==0:
#             return 1 + func(list1[1:])
#         else:
#             return 0 + func(list1[1:])

# print(func(list1))


#reversing a string using the recursion

# str1="pratik"

# def func(str1):
#     if len(str1)==1:
#         return str1[0]
#     else:
#         return str1[-1]+func(str1[:-1])

# print(func(str1))


#finding the fibonaci series using the recursion approach 

def func(n):
    if n ==0:
        return 0
    if n==1:
        return 1
    else:
        return func(n-1)+func(n-2)

result =[]
for i in range(10):
    result.append(func(i))

print(result)