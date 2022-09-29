import re 

pattern=re.compile("(\d*\.?\d*)")

str1="AC*wv12n/:#e123we2.45oin (fwoi6n#a98nfwb+owi"

iter_match=pattern.finditer(str1)

result=[]
for match in iter_match:
    result.append(match.group())

result=list(filter(lambda x:x if type(x)==str else 0,result))
result=list(map(lambda x:int(x) if x.isdigit() else float(x),result))
result.sort()
print(result)

# print(float('2.45'))