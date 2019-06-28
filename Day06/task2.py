import requests

try:
    response = requests.get("https://t1.huanqiucdn.cn/081f78a20214d0e009cda79106046a95.jpg")
    if response.status_code == 200:
        with open("a.jpg", "wb")as f:
            f.write(response.content)
except Exception as e:
    print(e)
