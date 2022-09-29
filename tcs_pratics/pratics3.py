input=[5,5,1,5,5,5]

count=0
def func(list1):
    global count
    if len(list1)==1:
        return count
    else:
        if list1[0]==list1[1]:
            count+=1
    func(list1[1:])

func(input)
print(count)