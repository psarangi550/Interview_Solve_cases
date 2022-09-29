#LCM of 2 numbers
def foo(num1,num2):
    if num1>num2:
        higher=num1
    if num2>num1:
        higher=num2
    value=higher
    while True:
        if higher%num1==0 and higher%num2==0:
            print("LCM of the number is", higher)
            break
        else:
            higher+=value

foo(2,3)

