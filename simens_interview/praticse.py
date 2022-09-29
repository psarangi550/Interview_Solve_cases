list1=["act","dog","god","tca","cat"]

dict1={}

for index,item in enumerate(list1):
    sorted_item="".join(sorted(item))
    # print(sorted_item)
    # print(index,item)
    if sorted_item in dict1:
        dict1[sorted_item]=dict1.get(sorted_item)+[index]
    else:
        dict1[sorted_item]=[index]
        

print(dict1)

