def foo(n1,n2):
    i=0
    if n1>n2:
        higher=n1
    elif n2>n1:
        higher=n2
    val=higher
    while True:
        i+=1
        if i>5:
            break
        else:
            if higher%n1==0 and higher%n2==0:
                print(higher)
        higher=higher+val
        

foo(2,4)
