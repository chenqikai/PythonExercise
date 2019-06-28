"""
排名、名字、导演、上映年份、国家、影片类型、评分、评价人数、短评
"""

import requests
from bs4 import BeautifulSoup
import time
import csv
import os

ranking = 1
with open("douban.csv", "w", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["排名", "名字", "图片地址", "评分"])
    urls = ['https://movie.douban.com/top250?start=' + str(index) + '&filter=' for index in range(0, 250, 25)]
    for url in urls:
        time.sleep(0.5)
        response = requests.get(url)
        response.encoding = "utf-8"
        html = BeautifulSoup(response.text, features="html.parser")
        content = html.find("ol", attrs={"class": "grid_view"})
        # 排名
        divs = content.find_all("div", attrs={"class": "item"})
        for div in divs:
            title = div.find("span", attrs={"class": "title"})
            titlestr = title.text  # 标题
            img = div.find("img", attrs={"width": "100"})
            srcstr = img.attrs["src"]  # 图片地址
            if os.path.exists("电影图片"):
                pass
            else:
                os.mkdir("电影图片")
            try:
                imgresponse = requests.get(srcstr)  # 图片
                with open("电影图片/" + str(ranking) + "." + titlestr + ".jpg", "wb") as f:
                    f.write(imgresponse.content)
            except Exception as e:
                print(e)
            rating_num = div.find("span", attrs={"class": "rating_num"})
            rating_numstr = rating_num.text
            csv_writer.writerow([ranking, titlestr, srcstr, rating_numstr])
            print([ranking, titlestr, srcstr, rating_numstr])
            ranking += 1
