import csv
from bs4 import BeautifulSoup
import bs4
import requests

try:

    with open("stock.csv", "a", newline="")as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(
            ["代码", "简称", "最新价(HKD)", "涨跌幅", "涨跌额", "5分钟涨幅", "成交量(手)", "成交额(万元)", "换手率", "振幅", "量比", "市盈率"])

        i = 1
        while True:
            # time.sleep(1)
            response = requests.get("https://quote.stockstar.com/stock/sha_3_1_" + str(i) + ".html")
            htm = BeautifulSoup(response.text, features="html.parser")
            #
            tbody = htm.find("tbody", attrs={"id": "datalist"})
            if isinstance(tbody, bs4.element.Tag):
                trs = tbody.find_all("tr")

                if len(trs) > 1:
                    for tr in trs:
                        tds = tr.find_all("td")
                        code = tds[0].text
                        name = tds[1].text
                        nowprice = tds[2].text
                        pricelimit = tds[3].text
                        changeamount = tds[3].text
                        increase = tds[3].text
                        turnover = tds[3].text
                        volumeoftransaction = tds[3].text
                        turnoverrate = tds[3].text
                        amplitude = tds[3].text
                        quantityrelativeratio = tds[3].text
                        PEratio = tds[3].text
                        csv_writer.writerow(
                            [code, name, nowprice, pricelimit, changeamount, increase, turnover, volumeoftransaction,
                             turnoverrate, amplitude, quantityrelativeratio, PEratio])
                    i += 1
                else:
                    break
            continue
except Exception as e:
    print(e)
