import requests
from bs4 import BeautifulSoup
import time
import csv
import os

index = 1
with open("meitu.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["标题", "超级链接"])
    urls = ["http://www.win4000.com/meinvtag352_" + str(index) + ".html" for index in range(1, 6)]
for url in urls:
    time.sleep(0.5)
    response = requests.get(url)
    response.encoding = "utf-8"
    html = BeautifulSoup(response.text, features="html.parser")
    content = html.find("div", attrs={"class": "Left_bar"})
    print(content)
    # lis = content.find_all("a", attrs={})
    imgs = content.find_all("img", attrs={})
    for img in imgs:
        title = img.attrs["title"]
        # titlestr = title.text
        srcstr = img.attrs["data-original"]
        if os.path.exists("美图"):
            pass
        else:
            os.mkdir("美图")
        try:
            imgresponse = requests.get(srcstr)
            with open("美图/" + title + ".jpg", "wb") as f:
                f.write(imgresponse.content)
        except Exception as e:
            print(e)

        print([title, srcstr])
        # csv_writer.writerow([title, srcstr])
        # f.close()