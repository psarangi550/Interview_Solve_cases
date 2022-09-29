# def foo(num1):
#     temp=num1
#     rev_num=0
#     while temp>0:
#         digit=temp%10
#         rev_num+=digit*digit
#         temp=temp//10
#     return rev_num

# def bar(num1):
#     if foo(num1)==1:
#         print("happy number")
#         return
#     elif foo(num1)==4:
#         print("unhappy number")
#         return
#     else:
#         num1=foo(num1)
#         return bar(num1)


# # bar(89)
# bar(13)


# def bar(num1):
#     temp=num1
#     rev_num=0
#     while temp>0:
#             # print(temp)
#             digit=temp%10
#             rev_num+=digit*digit
#             temp=temp//10
#     return rev_num

# def foo(num1):
#     while True:
#         if bar(num1)==1:
#             print("happy")
#             break
#         elif bar(num1)==4:
#             print("unhappy")
#             break
#         else:
#             val=bar(num1)
#             return foo(val)
            

# foo(13)
# foo(89)
# foo(31)
# foo(14)
# foo(19)

#alternate approach 

# num=int(input("enter a number"))
# temp=num
# while sum!=1 and sum!=4:
#     sum=0
#     while temp!=0:
#         digit=temp%10
#         sum+=digit*digit
#         temp=temp//10
#     temp=sum
# if sum==1:
#     print("happy number")
# else:
#     print("unhappy number")

#alternate approch

def foo(num):
    sum=None
    temp=num
    while sum!=1 and sum!=4:
        sum=0
        while temp!=0:
            digit=temp%10
            sum+=digit*digit
            temp=temp//10
        temp=sum
    if sum==1:
        print("happy number")
    else:
        print("unhappy number")

foo(13)