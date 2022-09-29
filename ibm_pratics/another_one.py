from collections import namedtuple,ChainMap,Counter

str1="python is awsome"

# # c=Counter(str1).most_common(2)

c1=list(Counter(str1).elements())

print(c1)
# print(dict(c))

# for i in c1:
#     print(i)

# # dict2={"name":"pratik"}

# # dict3={"mark":100}

# # print(ChainMap(dict2,dict3))

# # color=namedtuple("Color",["red","green","blue"])

# # white=color(red=100,green=200,blue=300)

# # print(white[0])

# # list1=[10,30,40]

# # print(color._make(list1))