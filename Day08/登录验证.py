import requests

from bs4 import BeautifulSoup

cookies = {

}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
response = requests.get("https://my.csdn.net/my/score", headers=headers, cookies=cookies)
html = BeautifulSoup(response.text, features="html.parser")
table = html.find("table", attrs={"class": "datatable"})
tbody = table.find("tbody")
trs = tbody.find_all("tr")

for tr in trs:
    tds = tr.find_all("td")
    score = tds[0].text
    src = tds[1].text
    reason = tds[2].text
    time = tds[3].text
    print([score, src, reason, time])
