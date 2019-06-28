import requests
from bs4 import BeautifulSoup
import time
import csv

with open("baisi.csv", "w", newline="")as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["编号", "昵称", "头像", "时间", "描述", "主图", "点赞数", "差评数", "分享数", "评论数"])

url = "http://www.budejie.com/"
response = requests.get(url)
with open("temp.txt", "w", encoding="utf-8")as f:
    f.write(response.text)
