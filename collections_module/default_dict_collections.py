from collections import defaultdict

str1="aaabbbcccddddd"

# d=defaultdict(int)

# for s in str1:
#     d[s]+=1

d=dict()
for s in str1:
    if s not in d:
        d[s]=1
    else:
        d[s]+=1

print(d)
