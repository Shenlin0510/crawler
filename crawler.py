#抓取網路PPT電影版網頁原始碼(HTML)
import urllib.request as req
def getData(ur1):


#建立一個request物件，附加 Request Headers的資訊
     request=req.Request(ur1,headers={
         "cookie":"over18=1",
          "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
     })
     with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
#解析原始碼
     import bs4
     root=bs4.BeautifulSoup(data,"html.parser")
     titles=root.find_all("div",class_="title")
     for title in titles:
    #if title.a!=None:  #如標題包含 a 標籤，印出來
        print(title.a.string)
     nextlink=root.find("a",string="‹ 上頁")
     return nextlink["href"]

pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
    #上一頁的網址
    pageURL="http://www.ptt.cc"+getData(pageURL)
    count+=1