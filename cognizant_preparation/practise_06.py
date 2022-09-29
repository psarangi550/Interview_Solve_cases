list1=[40,10,20,30,30,4,100]

# # def foo(list1):
# #     max_num=list1[0]
# #     for ele in list1:
# #         if ele>max_num:
# #             max_num=ele
# #     list1.remove(max_num)
# #     return max(list1)

# # print(foo(list1))

# def bar(list1):
#     if list1[0]>list1[1]:
#         first=list1[0]
#         second=list1[1]
#     else:
#         first=list1[1]
#         second=list1[0]
#     for i in range(2,len(list1)):
#         if list1[i]>first:
#             second=first
#             first=list1[i]
#         elif list1[i]!=first and list1[i]>second:
#             second=list1[i]
#     return second

# print(bar(list1))

# def func(num):
#     temp=num
#     arm_number=0
#     while temp>0:
#         digit=temp%10
#         arm_number+=digit**3
#         temp=temp//10
#     print(arm_number)
#     if num==arm_number:
#         print("armstrong")
#     else:
#         print("not a armstrong")

# func(153)

def func(num):
    temp=num
    arm_number=0
    while temp>0:
        digit=temp%10
        arm_number+=digit
        temp=temp//10
    return arm_number

print(func(153))

