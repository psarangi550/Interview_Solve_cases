str1="daabcbaabcbc"
sub_str="abc"

import re 
def foo(str1,sub_str):
    list1=list(str1)
    pattern=re.compile("abc")
    iter_match=pattern.finditer(str1)
    for item in iter_match:
        for i in range(*item.span()):
            list1[i]=""
    return "".join(list1)

result=""
def bar(str1,sub_str):
    global result
    if str1.count(sub_str)==0:
        return result
    else:
        result=foo(str1,sub_str)
    return bar(result,sub_str)
    
print(bar(str1,sub_str))
