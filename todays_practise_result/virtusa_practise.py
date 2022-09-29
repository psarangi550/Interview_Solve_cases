list1=["ab","abc","defge","efghikl","pqrstuvw","def"]
list2=[]

def foo(list1):
    # list1.sort(key=lambda x:len(x))
    for index,ele in enumerate(list1):
        if len(ele)>3:
            first=ele[:3]
            list2.append(first)
            second=ele[3:]
            if len(second)>=3:
                # print([second if x==index else "" for x in range(len(list1))])
                foo([second if x==index else "" for x in range(len(list1))])
            else:
                list2.append(second)
        else:
            if ele !="":
                # print(ele)
                list2.append(ele)

foo(list1)
print(list2)
    

