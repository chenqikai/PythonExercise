from bs4 import BeautifulSoup
import requests

proxies = {
    "http": "http://60.9.1.81:80",
}

response = requests.get("http://ip.tool.chinaz.com", proxies=proxies)
html = BeautifulSoup(response.text, features="html.parser")
ipaddress = html.find("dd", attrs={"class": "fz24"})
print(ipaddress.text)
