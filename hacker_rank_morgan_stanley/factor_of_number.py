def foo(num):
    temp=num
    result=[]
    while temp>0:
        digit=temp%10
        if digit!=0:
            if num%digit==0:
                result.append(digit)
        temp=temp//10
    return len(result)

print(foo(111))
print(foo(12))
print(foo(111))

