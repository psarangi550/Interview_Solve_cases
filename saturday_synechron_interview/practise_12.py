list1=[10,20,30,40]
# print(dict((enumerate(list1))))

def foo(func):
    def bar(dict1):
        dict1=func(dict1)
        return {k:v for k, v in sorted(dict1.items())}
    return bar

@foo
def home(dict1):
    return dict1

dict1={1: 20, 2: 30, 3: 40,0: 10}

# print(foo(dict1))

print(home(dict1))