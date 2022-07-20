from collections import defaultdict

str1="aaabbbcccddddd"

d=defaultdict(int)

for s in str1:
    d[s]+=1

print(d)
