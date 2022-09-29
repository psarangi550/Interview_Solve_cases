i = 2
result = []

def func(n1, n2):
    global i
    global result
    if n1 > n2:
        if i > n2:
            return max(result)
        if n1 % i == 0 and n2 % i == 0:
            result.append(i)
    elif n2 > n1:
        if i > n1:
            return max(result)
        if n1 % i == 0 and n2 % i == 0:
            result.append(i)
    i+=1
    return func(n1, n2)


print(func(8, 12))
