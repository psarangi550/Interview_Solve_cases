from collections import defaultdict
str1="indianPythonista"
d=defaultdict(lambda :0)
for ele in str1:
    d[ele]+=1
print(dict(d))