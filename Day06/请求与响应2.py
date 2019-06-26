import requests

try:
    response = requests.get("http://china.cnr.cn/news/20190626/t20190626_524663951.shtml")
    response.encoding = "utf-8"
    print(response.text)
    with open("a.html", "w", encoding="utf-8")as f:
        f.write(response.content)
except Exception as e:
    print(e)
