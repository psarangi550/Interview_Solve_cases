input="This_Is_A_Good_Morning"

def foo(str1):
    result = ""
    input_list=str1.split("_")
    for ele in input_list:
        result+=f"{''.join([item.upper() if item.islower() else item.lower() for item in ele])}."
    return result

print(foo(input))

