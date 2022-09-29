def foo(num):
    temp=num
    rev_num=0
    while temp>0:
        digit=temp%10 #121%10==21
        rev_num=rev_num*10+digit
        temp=temp//10
    if num==rev_num:
        print("pallendrom")
    else:
        print("not a pallendrom")

foo(12321)