import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"


html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class": "column"},limit= 20)


count = 1

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
    newprice = li.find("ins").text.strip().strip("TL")
    
    
    print (f"{count}-Name: {name}\nLink: {link}\nOld Price: {oldprice}\nNew Price: {newprice}")
    count+=1


