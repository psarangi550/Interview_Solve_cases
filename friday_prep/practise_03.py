str1="daabcbaabcbc"
sub_str="abc"
# result="dabaabcbc"--->"dababc"--->"dab"
result=""
def foo(str1,sub_str):
    global result
    for i in range(0,len(str1)):
        if str1.count(sub_str)==0:
            return result
        else:
            index=str1.find(sub_str)
            result=str1[:index]+str1[index+len(sub_str):]
            break
    return foo(result,sub_str)

print(foo(str1,sub_str))
        