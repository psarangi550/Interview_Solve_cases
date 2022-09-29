def foo(num):
    a,b=1,1
    i=0
    while i<num:
        yield a
        a,b=b,a+b
        i+=1

for i in foo(10):
    print(i)