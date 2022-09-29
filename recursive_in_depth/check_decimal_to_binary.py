result= []

i=2
def func(num):
    global i
    if num==0:
        return "".join(list(map(str,result)))
    else:
        result.append(num%i)
        num=num//i
    return func(num)

print(func(9))