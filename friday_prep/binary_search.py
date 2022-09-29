#Binary Search 
list1=[-1,0,3,5,9,12]
def foo(list1,target):
    start=0
    end=len(list1)-1
    while start<=end:
        mid=(start+end)//2
        num=list1[mid]
        if num==target:
            return mid
        elif target>num:
            start=mid+1
        elif target<num:
            end=mid-1  

print(foo(list1,9))
        

