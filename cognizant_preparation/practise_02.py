str1="aabbccddaaeppqqq"

# def foo(str1):
#     count=1
#     result=""
#     for i in range(len(str1)-1):
#         if str1[i]==str1[i+1]:
#             count+=1
#         else:
#             result+=str1[i]+str(count)
#             count=1
#     result+=str1[-1]+str(count)
#     return result

# print(foo(str1))

#using the while

# def foo(str1):
#     count=1
#     result=""
#     i=0
#     while(i<len(str1)-1):
#         if str1[i]==str1[i+1]:
#             count+=1
#         else:
#             result+=str1[i]+str(count)
#             count=1
#         i+=1
#     result+=str1[-1]+str(count)
#     return result

# print(foo(str1))



# def foo(str1):
#     count=0
#     result=[]
#     temp=list(str1)
#     n=len(temp)
#     for i in range(n):#a
#         for j in range(i,n):#abbccddaaeppq
#             if temp[i] in result or temp[j] in result:
#                 continue
#             else:
#                 if temp[i]==temp[j]:
#                     count+=1
#                 else:
#                     continue
#         if temp[i] in result or temp[j] in result:
#             continue
#         else:
#             result.extend((temp[i],str(count)))
#         count=0

#     return "".join(result)

# print(foo(str1))



# def foo(str1):
#     count=1
#     result=""
#     temp=list(str1)
#     print(temp)
#     i=0
#     while i<len(temp)-1:
#         while i<len(temp)-1 and temp[i]==temp[i+1]:
#             count+=1
#             i+=1
#         result+=temp[i]+str(count)
#         count=1
#         i+=1
#     if temp[-1]==temp[-2]:
#         pass
#     else:
#         result+=temp[-1]+str(count)
#     return result

# print(foo(str1))
        

