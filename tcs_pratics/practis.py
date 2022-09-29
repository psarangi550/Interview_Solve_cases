input=[
    {"name":"Rohan","location":"l1"},
    {"name":"Mohan","location":"l2"},
    {"name":"Arjun","location":"l1"},
    {"name":"Mohith","location":"l3"},
    {"name":"Mohith","location":"l2"}
]

result=[]
output={}
for ele in input:
    key=ele.get("location")
    if key in output:
        output.get(key).append({"name":ele.get("name"),"location":ele.get("location")})
    else:
        output[key]=[{"name":ele.get("name"),"location":ele.get("location")}]

print(output)