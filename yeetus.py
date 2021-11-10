from lxml import etree
import requests
from bs4 import BeautifulSoup

messageBody = "bunghole"

URL = "https://www.urbandictionary.com/define.php?term=" + str(messageBody)
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="meaning")

# for i in results:
#     print(i)

# gum = etree.HTML(str(soup))
# results = gum.xpath('//*[@id="content"]/div[1]/div[3]/a[1]')[0].text
print(results.text)
