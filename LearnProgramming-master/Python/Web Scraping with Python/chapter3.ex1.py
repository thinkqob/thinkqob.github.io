from urllib.request import urlopen
from bs4 import BeautifulSoup

def getLinks(startPage):
    html = urlopen(startPage)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.findAll("div", {"class":"photo-wrapper-inner"})

links = getLinks("http://thinkqob.tumblr.com")
for link in links:
    print(link.img['src'])
