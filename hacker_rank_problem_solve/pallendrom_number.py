def foo(num):
    temp=num
    rev_num=0
    while(temp>0):
        digit=temp%10
        rev_num=rev_num*10+digit
        temp=temp//10
    if num==rev_num:
        return True
    else:
        return False

print(foo(1234321))