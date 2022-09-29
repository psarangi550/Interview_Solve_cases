list1=[100,40,20,30,50,70,60,50]


min=list1[0]
def func(list1):
    global min
    if len(list1) ==0:
        return min
    else:
        if list1[0]<=min:
            min=list1[0]
    return func(list1[1:])

print(func(list1))


# #alternate approach for finding min or max is 

# def func2(list1):
#     if len(list1)==1:
#         return list1[0]
#     else:
#         return min(list1[0],func2(list1[1:]))


# def func3(list1):
#     if len(list1)==1:
#         return list1[0]
#     else:
#         return max(list1[0],func2(list1[1:]))
# # print(func3(list1))


# list2=["cat","mat","dinosur","elephant","hippo","dracula","crocodile"]

# def func4(list2):
#     if len(list2)==1:
#         return list2[0]
#     else:
#         result=min(list2[0],func4(list2[1:]))
#     return result


# print(func4(list2))


# # print("cat">"Dinosur")


# # str1="elementmanager"

# # def func5(str1):
# #     if str1.count("e")==0:
# #         return str1
# #     else:
# #         print(str1.count("e"))
# #         index=str1.index("e")
# #         str1=str1[index+1:]
# #     return func5(str1)

# # print(func5(str1))


# #recursion fibo

# a,b=0,1
# c=0
# result=[]
# def fibo(n):
#     global result
#     global a
#     global b
#     global c
#     if n==0:
#         return result
#     else:
#         c=a+b
#         result.append(a)
#         a=b
#         b=c
#     return fibo(n-1)

# # print(fibo(5))

# #optimizing the same 


# def fibo_iter(n):
#     a,b=0,1
#     for _ in range(n):
#         a,b=b,a+b
#     return a

# # print(fibo_iter(5))
# result=[]
# for i in range(5):
#     result.append(fibo_iter(i))

# print(result)




# # from itertools import accumulate
# # iter_val=accumulate(range(101))
# # for val in iter_val:
# #     print(val)


# from iteration_utilities import flatten
# l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
# print(list(flatten(l)))


# import more_itertools