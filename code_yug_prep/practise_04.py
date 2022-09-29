list1=["cat","dog","god","tca","act"]
def foo(list1):
    dict1={}
    for i in range(len(list1)):
        word="".join(sorted(list1[i]))
        if word not in dict1:
            dict1[word] =[i+1]
        else:
            dict1[word].append(i+1)
    return dict1

print(foo(list1))



