def foo(num):
    if num%15==0:
        print("fizzbuzz")
    elif num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
    else:
        print(num)


def foo(num):
    result=""
    dict1={3:"fizz",5:"buzz"}
    val=None
    for k,v in dict1.items():
        if num%k==0:
            result+=v
        else:
            continue
    return result

print(foo(30))


foo(30)