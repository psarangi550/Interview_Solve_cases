dict1={chr(96+k):{k**2:k**3} for k in range(1,4)}
print(dict1)
result=[]
output=[]
def foo(dict1):
    for ele in dict1:
        if type(dict1[ele])==dict:
            foo(dict1[ele])
        else:
            result.append(ele)
        # result.append(ele)
        output.append(ele)
    return list(set(output+result))

print(foo(dict1))
# print(result)