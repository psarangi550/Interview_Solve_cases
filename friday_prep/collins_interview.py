str1="1:Mark:0, 2:David:1, 3:Harry:1, 4:Bob:2, 5:Jenny:2, 6:Pete:3"
list1=str1.split(", ")
result=[]
for ele in list1:
    item=ele.split(":")
    result.append(item)
dict1={ ele[0]:ele[1] for ele in result }
print(dict1)
list2=[ele[2] for ele in result]
print(list2)
i=-1
ch=""
val=""
for ele in dict1:
    i+=1
    if ch==dict1.get(list2[i]):
        result=[]
        result.extend(((dict1.get(ele)),val))
        print(f"{dict1.get(list2[i])} managing for {result}")
    else:
        result=[]
        ch=dict1.get(list2[i])
        print(f"{dict1.get(list2[i])} managing for {result}")
    val=dict1.get(ele)

# Mark:
# - David
# - Harry

# David:
# - Bob
# - Jenny

# Harry:
# - Pete

# Bob:
# -Jenny:
# -Pete:

