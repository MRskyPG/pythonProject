#pip install beautifulsoup4 lxml
from bs4 import BeautifulSoup

with open ("blank/index2.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title.text)

# .find(...) - the first object with name ... from (...) , but .find_all() - all objects with name ... adds to list.

page_h1 = soup.find_all("h1")

for item in page_h1:
    print(item.text)