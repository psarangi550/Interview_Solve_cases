list1 = [1, 1, 1, 2, 4, 8, 3, 9, 27, 4, 16, 64]
result=[]
list2=[result.extend((x,x**2,x**3)) for x in range(1,4)]
print(result)

# result=[]
# count=0
# for x in range(1, 4):#1
#     count+=1
#     for y in range(x):#1
#         if x>1:
#             result.append(count)
#             result.append(count**2)
#             result.append(count**3)
#             break
#         else:
#             result.append(count)
#             result.append(count**2)
#             result.append(count**3)

# print(result)
    
