import re

str1="python interview with .tcs"

val=re.split("\.",str1)

result=[]

for index_val,item in enumerate(val):
    if " " in item and index_val==0:
        result.append(item.split()[0])
    else:
        result.append(item.split()[-1])

print(result)
