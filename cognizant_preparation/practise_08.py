input="aaabbbcccaa " 
output="3a3b3c2a"

def foo(str1):
    count=1
    result=""
    for i in range(len(str1)-1):
        if str1[i]==str1[i+1]:
            count+=1
        else:
            result+=str1[i]+str(count)
            count=1
    if str1[-1]==" ":
        pass
    else:
        result+=str1[i]+str(count)
    return result

print(foo(input))
