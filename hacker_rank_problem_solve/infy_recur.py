st1="aba"
n=10

def foo(st1):
    if len(st1)==n:
        return st1
    else:
        st1+=st1[0]
        
    return foo(st1)


print(foo(st1))