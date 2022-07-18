import requests
from collections import OrderedDict
output=[]
result=[]

def get_max_sub(dict1):
    return dict["submission_count"]
        

def getUsernames():
    resp=requests.get("https://jsonmock.hackerrank.com/api/article_users")
    resp_dict=resp.json()["data"]
    for user in resp_dict:
        result.append({"count":user["submission_count"],"name":user["username"]})
    # result.append(output)
    new_resp=requests.get("https://jsonmock.hackerrank.com/api/article_users/2")
    new_resp_dict=resp.json()["data"]
    for user in new_resp_dict:
        result.append({"count":user["submission_count"],"name":user["username"]})
    new_lst=sorted(result, key=lambda d: d['count'],reverse=True)
    return list(set(new_lst))
    # for res in newlist:
    #     output.append(res["name"])
    # return output

    
    
    # result.append(output)
    # return result

if __name__ == "__main__":
    print(getUsernames())