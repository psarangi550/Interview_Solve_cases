# using the recursive approach

result = []
a, b = 0, 1
c = 0
def fibo(n):
    global a
    global b
    global c
    global result
    if n == 0:
        return result
    else:
        result.append(a)
        c = a + b
        a = b
        b = c
    return fibo(n - 1)


# if __name__ == "__main__":
#     print(fibo(15))


# using the iterative approach

output = []


def fibo_iter(n):
    a, b = 0, 1
    i = 0
    while i < n:
        c = a + b
        yield a
        a = b
        b = c
        i += 1


for i in fibo_iter(15):
    output.append(i)

if __name__ == "__main__":
    print(output)
