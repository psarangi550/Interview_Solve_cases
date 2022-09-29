import re 
list1=["1234python668","678java899","4566hadoop9123"]
pattern=re.compile("\d")

def bar(list1):
    result=[]
    for ele in list1:
        output=foo(ele)
        result.append(output)
    print(result)

def foo(str1):
    output=""
    iter_match=pattern.finditer(str1)
    for item in iter_match:
        output+=item.group()
    return output

# print(foo("1234python668"))

bar(list1)