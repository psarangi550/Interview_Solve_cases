# from collections import Counter
str1="aabbccderefffeee"
# c=Counter(str1)
# print(c.most_common()[-1])

dict1={}

for ele in str1:
    if ele not in dict1:
        dict1[ele]=1
    else:
        dict1[ele]+=1
# print(dict1)
dict2={k:v for k,v in sorted(dict1.items(),key=lambda v:v[1])}
print(min(dict2,key=dict2.get))
