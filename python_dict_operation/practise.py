# from itertools import permutations
# str1="CAT"
# iter_str=permutations(str1,len(str1))
# count=0
# value_list=("",)*len(str1)
# # print(value_list)
# for value_list in iter_str:
#     if value_list[0] not in ["A","E","I","O","U"]:
#         count+=1
#         print(*value_list)
    
# print(count)


# tup_1=[]


from ast import operator


dict1={
    "Animal":"Dog",
    "Fruit":"Pear",
    "Vegetable":"cabbage",
    "Tree":"Maple",
    "Flower":"Daisy"
}

# dict2={k:v for k,v in sorted(dict1.items(),reverse=True)}

# print(dict2)
l1=list(dict1.items())
l2=l1[::-1]
print(dict(l2))
# print(l1)