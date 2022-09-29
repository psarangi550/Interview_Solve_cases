def fibo(n):
    a,b=0,1
    if n<1:
        print(b)
    else:
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

fibo(20)
