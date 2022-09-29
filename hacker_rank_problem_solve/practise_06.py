# output=[]
# def foo():
#     temp=1
#     result=[]
#     for i in range(3):
#         result=list()
#         for j in range(3):
#             result.append(temp)
#             temp=temp+1
#         output.append(result)
#         print()
#     return output

# final=foo()

final=[[1,2,3],[4,5,6],[9,8,9]]

# print(final)

sum=0
total=0
for i in range(len(final)):
    for j in range(len(final)):
        if i == j:
            sum+=final[i][j]
        if (i+j)==2 or i==j==len(final)//2:
            # print(i,j)
            total+=final[i][j]

print(sum)
print(total)
print(total-sum)

