def foo(num):
    temp=num
    digit=None
    sum_val=0
    while temp>0:
        digit=temp%10
        sum_val=sum_val+(digit**3)
        temp=temp//10
    if num==sum_val:
        print("Armstrong")
    else:
        print("Not an ArmStrong Number")

foo(354)
