list1=[[1,2,3],[4,5,6],[7,8,9]]
# result=[]
# count=0
# for n in range(len(list1)*2-1):
#     for i in range(len(list1)):
#         for j in range(len(list1)):
#             if i==j:
#                 print(list1[j][i],end="")
#                 break
#     break
#     print()

def foo(list1):
    result=[]
    for i in range(len(list1)):
        temp=[]
        for j in range(len(list1[i])):
            print(list1[j][i],end="")
            temp.append(list1[j][i])
        result.append(temp)
        print()
    
    for i in range(len(result)-1,-1,-1):
        for j in range(len(result[i])):
            print(result[i][j],end="")
        print()

    # return result[::-1]

print(foo(list1))