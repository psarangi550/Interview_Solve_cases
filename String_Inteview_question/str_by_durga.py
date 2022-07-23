str1="aaaabbbccz"

# output=""
# result=0
# def func(str1):
#     global result
#     global output+str[]
#     if len(str1)==1:
#         return str1[0]
#     else:
#         if (str1[0]==str1[1]):
#             result+=1
#         else:
#             output+=str(result)+str1[0]
#             result=0
#     return func(str1[1:])

# func(str1)
# print(output)


from collections import Counter

c=Counter(str1)

output=""
for key,value in c.items():
    output+=key+chr(65+value)

print(output)