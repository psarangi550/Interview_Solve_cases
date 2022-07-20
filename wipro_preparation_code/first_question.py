items=int(input("Enter the Number of Items"))
products_price=list(map(int,input("Enter the product unit available in the warehouse").strip().split()))
products_sku=list(map(int,input("Enter the product unit available in the warehouse").strip().split()))
distance=list(map(int,input("Enter the distance ex if 3000 then enter 3").strip().split()))

result=[]
for i in range(items):
    if products_sku[i]>0:
        result.append(products_price[i]*distance[i])

print(result)
# print(" ".join(result))

