from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string


def cleanInput(in_put):
    in_put = re.sub('\n+', " ", in_put)
    in_put = re.sub('\[[0-9]*\]', " ", in_put)
    in_put = re.sub(' +', " ", in_put)
    in_put = bytes(in_put, "UTF-8")
    in_put = in_put.decode("ascii", "ignore")
    cleanInput = []
    in_put = in_put.split(' ')
    for item in in_put:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def ngrams(in_put, n):
    in_put = cleanInput(in_put)
    output = []
    for i in range(len(in_put)-n+1):
        output.append(in_put[i:i+n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
in_put = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = ngrams(in_put, 2)
print(ngrams)
print("2-grams count is: "+str(len(ngrams)))
