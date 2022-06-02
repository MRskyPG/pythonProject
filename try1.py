import re
from bs4 import BeautifulSoup
import requests

#Блок 1. Если еще нет html-файла по сайту, делаем закоментированный блок без всего остального ниже. После комментируем этот блок и читаем файл.
# url = "https://ru.m.wikipedia.org/wiki/Tesla"
#
# headers = {
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# "User-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open("blank/tesla.html", "w", encoding="utf-8") as file:
#     file.write(src)

with open("blank/tesla.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

name = soup.find("div", class_="page-heading").text.strip()





