def foo(a,b):
    if b==0:
        return a
    return foo(b,a%b)

# def bar(a,b):
    # return (a*b)//foo(a,b)



# print(bar(24,36))

print(foo(4,8))
