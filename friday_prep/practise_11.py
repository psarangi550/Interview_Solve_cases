str1="nitin"

def foo(str1):
    result=True
    for i in range(len(str1)//2):
        if str1[i]==str1[len(str1)-1-i]:
            continue
        else:
            print("not a pallendrom")
            result=False
            break
    if result:
        print("pallendrom")


foo("pratik")

