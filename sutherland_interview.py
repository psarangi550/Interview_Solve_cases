list1=[]
s_str1=""
def func(str1):
    global list1
    global s_str1
    s_str1 ="".join(sorted(str1))
    if len(s_str1) == 1:
        list1.append(str1)
        print("".join(list1))
    else:
        if s_str1[0] == s_str1[1]:
            list1.insert(0,s_str1[0])
            list1.insert(-1,s_str1[1])
            s_str1 = s_str1[1:]
        else:
            list1.append(s_str1[0])
            s_str1 = s_str1[1:]
        func(s_str1)


func("moon")
