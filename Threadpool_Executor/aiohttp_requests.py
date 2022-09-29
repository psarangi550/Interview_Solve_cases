import asyncio
import requests

async def get_data():
    task=asyncio.create_task(get_resp())
    await task
    print(task)

async def get_resp():
    data={"name":"pratik"}
    resp=requests.get("https://httpbin.org/get",params=data)
    if resp.status_code == 200:
        return resp.json()

asyncio.run(get_data())