from collections import Counter

list1=[1,1,2,2,3]

c=Counter(list1)

result=[]

result=sorted(c.most_common(),key=lambda x:x[0])

for ele,count in result:
    print(ele,count)
    



