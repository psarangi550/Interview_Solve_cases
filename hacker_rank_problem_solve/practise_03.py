from collections import Counter

arr=[1,1,2,2,3]

c=Counter(arr)

result=[]
for val,occure in c.most_common():
    result.append((occure))
    max_occure=max(result)
    if max_occure==occure:
        print(val,occure)


