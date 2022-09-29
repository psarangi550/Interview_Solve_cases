list1=[1,1,2,3,5,8]
str1="abcdef"

result=str(sum(list1))
for index,ele in enumerate(str1):
    result+=str(list1[index])+ele

print(result)