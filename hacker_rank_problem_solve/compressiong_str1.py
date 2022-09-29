str1="aabbccaaafffeiii"
def foo(str1):
    count=1
    result=""
    for i in range(len(str1)-1):
        if str1[i]==str1[i+1]:
            count += 1
        else:
            result+=str1[i]+str(count)
            count=1
    result+=str1[-1]+str(count)
    return result

print(foo(str1))

#using the while loop in this case

def foo(str1):
    count=1
    result=""
    i=0
    while i<(len(str1)-1):
        if str1[i]==str1[i+1]:
            count+=1
        else:
            result+=str1[i]+str(count)
            count=1
        i+=1
    result+=str1[-1]+str(count)
    return result

print(foo(str1))