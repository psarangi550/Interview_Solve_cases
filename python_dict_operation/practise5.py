list1=[
    {
        "name":"pratik",
        "age":29,
        "mark":50
    },
    {
        "name":"rika",
        "age":23,
        "mark":100
    },
    {
        "name":"abi",
        "age":24,
        "mark":150
    }
]

list1.sort(key=lambda x:x["name"])

print(list1)