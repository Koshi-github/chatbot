from bs4 import BeautifulSoup
import requests

def MessageCreate(message):
    returnList =[]
    url ="https://www.kurashiru.com/search?query=" + str(message)

    html_doc  = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')

    returnList.append("「" + str(message) + "」を検索するニャン！")
    dlyLinkTags = soup.find_all("a",{"class":"DlyLink title"})

    if len(dlyLinkTags) <= 0:
        returnList.append("見つからなかったニャン…")
    else:
        returnList.append(url)
        returnList.append("このページが見つかったニャン！")

    return returnList