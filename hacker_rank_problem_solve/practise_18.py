# st1="UDDDUDUU"
st1="DDUUUUDD"

def foo(str1):
    vally_count=sea_level=0
    dict1={"U":1,"D":-1}
    for ele in str1:
        sea_level+=dict1[ele]
        if sea_level==0 and ele=="U":
            vally_count+=1
    print(vally_count)

foo(st1)

