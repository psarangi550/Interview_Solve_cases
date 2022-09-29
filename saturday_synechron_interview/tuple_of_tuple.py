list1=["cat","dog","god","tca","act"]

def foo(list1):
    dict1={}
    for ele in list1:
        val="".join(sorted(ele))
        if val not in dict1:
            dict1[val]=[list1.index(ele)]
        else:
            dict1[val].append(list1.index(ele))
    return dict1

print(foo(list1))