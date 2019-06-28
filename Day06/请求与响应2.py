import requests

response = requests.get("http://china.cnr.cn/news/20190626/t20190626_524663951.shtml")
response.encoding = "utf-8"
# print(response.text)
with open("a.html", "w", encoding="utf8")as f:
    f.write(response.text)
