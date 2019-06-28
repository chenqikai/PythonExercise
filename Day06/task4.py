import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}

response = requests.get("http://www.xinhuanet.com/politics/2019-06/25/c_1124669748.htm", headers=header)
response.encoding = "utf-8"
with open("b.html", "w", encoding="utf-8") as f:
    f.write(response.text)
