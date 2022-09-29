list1=[2,7,11,15]
target=9

def foo(list1, target):
    left=0
    right=len(list1)-1
    for ele in list1:
        if list1[left]+list1[right]>target:
            right=right-1
        elif list1[left]+list1[right]<target:
            left=left+1
        elif list1[left]+list1[right]==target:
            print("arr position is ", left, right)
            right=right-1
            left=left+1
            break

foo(list1,target)

