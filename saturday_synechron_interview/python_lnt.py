import time

start=time.perf_counter()

def foo(num):
    for j in range(1, num):
        for i in range(2,j//2+1):
            if j%i==0:
                break
        else:
            print(j)

foo(13)

end=time.perf_counter()-start

print(end)