def foo(num):
    temp=num
    result=True
    rev_num=0
    while temp>0:
        if temp%2==0:
            rev_num+=1
        else:
            if num!=1:
                result=False
            else:
                result=True
            break
        temp=temp//2
    if rev_num:
        return True
    else:
        return result

print(foo(1))
print(foo(512))

