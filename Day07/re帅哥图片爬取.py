import csv, time
import re

from bs4 import BeautifulSoup
import bs4
import requests

try:

    with open("帅哥.csv", "w", newline="")as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(
            ["标题", "连接", "评论", "点赞"])

        i = 1
        while True:
            # time.sleep(1)
            if i == 1:
                url = "http://www.shuaia.net/zhengtai/index.html"
            else:
                url = "http://www.shuaia.net/zhengtai/index_" + str(i) + ".html"

            response = requests.get(url)
            html = BeautifulSoup(response.text, features="html.parser")
            #
            title = html.find("h2", attrs={"class": "item-title"})
            title = title.find_all("a")
            re_link = re.compile(r'<img width="250" height="317" src="(.*?)" class="attachment-weiran"', re.S)
            # re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
            link = re_link.findall(html.text)
            link = link.find_all("span")
            good = html.find("a", attrs={"class": "heart-this"})
            good = good.find_all("span")

            print(title, link, good)
            # if isinstance(tbody, bs4.element.Tag):
            #     trs = tbody.find_all("tr")
            #
            #     if len(trs) > 1:
            #         for tr in trs:
            #             tds = tr.find_all("td")
            #             code = tds[0].text
            #             name = tds[1].text
            #             nowprice = tds[2].text
            #             �ǵ��� = tds[3].text
            #             �ǵ��� = tds[3].text
            #             �����Ƿ� = tds[3].text
            #             �ɽ��� = tds[3].text
            #             �ɽ��� = tds[3].text
            #             ������ = tds[3].text
            #             ��� = tds[3].text
            #             ���� = tds[3].text
            #             ��ӯ�� = tds[3].text
            #             csv_writer.writerow([code, name, nowprice, �ǵ���, �ǵ���, �����Ƿ�, �ɽ���, �ɽ���, ������, ���, ����, ��ӯ��])
            #         i += 1
            #     else:
            #         break
            # continue
except Exception as e:
    print(e)
