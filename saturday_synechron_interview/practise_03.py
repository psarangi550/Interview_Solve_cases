def foo(num):
    temp=num
    rev_num=0
    while temp>0:
        digit=temp%10
        rev_num+=digit**3
        temp=temp//10
    if rev_num==num:
        return "Armstrong"
    else:
        return "Not an Armstrong"

print(foo(153))