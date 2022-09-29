from operator import itemgetter

list1=[
    {"name":"pratik","age":30},
    {"name":"abi","age":20},
]

# list1.sort(key=itemgetter('name'),reverse=True)

# print(list1)

dict1={"USA":328_200_000,"France":67_000_000,"China": 1_393_000_000}

print({k:v for k,v in sorted(dict1.items(),key=lambda v:v[1])})

