def foo(num):
    result=""
    dict1={3:"fizz",5:"buzz"}
    for ele in dict1:
        if num%ele==0:
            result+=dict1[ele]
    return result

print(foo(3))
print(foo(5))
print(foo(15))
            