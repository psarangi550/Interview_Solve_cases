def foo(str1):
    dict1={}
    i=0
    result=0
    output=""
    for j in range(len(str1)):
        if str1[j] in dict1:
            i=max(i,(dict1[str1[j]]+1))
        else:
            result=max(result,(j-i+1))
            output=str1[i:j+1]
            dict1[str1[j]]=j
    return output

print(foo("bbbbbb"))