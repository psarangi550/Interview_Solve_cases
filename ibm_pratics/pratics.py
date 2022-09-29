st1="NAINA"
st2="REENE"

print(set(dict.fromkeys(st1)))

# for i in range(len(st1)):
#     if st1[i]==st2[i]:
#         print(st1[i])

str1="Hello There how you doing ! how life treating you"
list1=str1.split()

dict1=dict()

for s in list1:
    if s not in dict1:
        dict1[s]=1
    else:
        dict1[s]+=1

print(dict1)
