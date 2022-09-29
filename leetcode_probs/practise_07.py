list1=[9099892323,9099892324,9099892325]

def outer_fun(func):
    def inner_func(list1):
        result=[]
        for ele in list1:
            result.append("+91"+str(ele))
        return result
    return inner_func


@outer_fun
def foo(list1):
    print(list1)

print(foo(list1))