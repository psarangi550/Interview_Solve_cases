# def fibo(num):
#     a,b=0,1
#     if num<=0:
#         print("invalid input")
#     elif num<=1:
#         print(a)
#         print(b)
#     else:
#         print(a)
#         print(b)
#         while b<num:
#             b,a=a+b,b
#             print(b)
# fibo(8)

# def pallendrom(num):
#     temp=num
#     rev_num=0
#     while temp>0:
#         digit=temp%10
#         rev_num=rev_num*10+digit
#         temp=temp//10
#     if rev_num==num:
#         print("pallendrom")
#     else:
#         print("not a pallendrom")

# pallendrom(12321)

#aabbcc

# def foo(str1):
#     i=0
#     count=1
#     result=""
#     while i<len(str1)-1:
#         if str1[i]==str1[i+1]:
#             count+=1
#         else:
#             result+=str1[i]+str(count)
#             count=1
#         i+=1
#     result+=str1[-1]+str(count)
#     return result

# print(foo("aabbcc"))

