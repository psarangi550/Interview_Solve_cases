input={
    "a":{"b":
    {"c":1
	}
	},
    "d":2,
    "e":4
}
result={}
text=""
count=1
def foo(dict1):
    global text
    global result
    count=0
    for item in dict1:
        if type(dict1[item])==dict:
            text+=item+"."
            count+=1
            foo(dict1[item])
        else:
            if count==0:
                result[text+item]=dict1[item]
            else:
                result[item]=dict1[item]

foo(input)
print(result)