import sys

import gc

gc.disable()
print(gc.isenabled())


print(sys.argv)

def foo(a,b):
    return int(a) + int(b)

def bar(a,b):
    return a + ' ' + b

# print(foo(sys.argv[1],sys.argv[2]))


# print(bar(sys.argv[1],sys.argv[2]))