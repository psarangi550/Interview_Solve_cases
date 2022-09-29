def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)

def foo(num):
    temp=num
    fact_digit=0
    while temp>0:
        digit=temp%10
        fact_digit+=fact(digit)
        temp=temp//10
    print(fact_digit)
    if num==fact_digit:
        return True
    else:
        return False

print(foo(145))



# print(fact(5))