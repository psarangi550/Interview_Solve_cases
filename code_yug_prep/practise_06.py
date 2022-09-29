def foo(str1):
    result=0
    size =len(str1)
    for i in range(size):
        num=ord(str1[i])-ord("A")+1
        result+=num*pow(26,size-1)
        size=size-1
    return result

print(foo("AB"))