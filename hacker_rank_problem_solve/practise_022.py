
def foo(str1):
    forward=""
    backward=""
    n=len(str1)//2
    for i in range(n):
        forward+=str1[i]
    for i in range(len(str1)-1,n,-1):
        backward+=str1[i]
    if forward==backward:
        return True
    else:
        return False

print(foo("niten"))



