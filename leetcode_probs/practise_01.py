str1="abbaca"
str1="azxxzy"

def foo(str1):
    temp=[]
    for ele in str1:
        if ele not in temp:
            temp.append(ele)
        else:
            if temp:
                temp.pop()
                continue

    return "".join(temp)

print(foo(str1))                 





