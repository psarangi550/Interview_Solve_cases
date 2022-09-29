from collections import Counter
str1="abccccdd"
total_length=len(str1)//2
c=Counter(str1)
result=0
print(c)
total=0
for key,val in c.items():
    if val==1 and total<1:
        total+=1
        result+=val
    elif val%2==0:
        result+=val
print(result)
    


