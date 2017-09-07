#code=utf8
#爬豆瓣首页图片

import socket,re,sys,os,urllib
import requests
from bs4 import BeautifulSoup

targetPath=r"E:\user\Github\test\pic"

# def __main__():
#     url="https://www.douban.com/"
#     proxies = {
#       "http": "http://127.0.0.1:11080",
#       "https": "http://127.0.0.1:11080",
#     }
#     headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
#     getPage(url,proxies,)

def saveFile(path):

    #检测路径有效性
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

    #设置图片路径
    pos=path.rindex('/')
    t=os.path.join(targetPath,path[pos+1:])
    return t

# def getPage(url,proxies):
#     r=requests.get(url=url,proxies=proxies)
#     data=r.text
#
#     for link,t in set(re.findall(r'(https:[^\s]*?(jpg|png|gif))',str(data))):
#         print(link,t)
#         try:
#             # urllib.request.urlretrieve(link,saveFile(link))
#             requests.request(saveFile(link),link)
#         except:
#             print('失败')

url="https://www.youtube.com/"
proxies = {
  "http": "http://127.0.0.1:11080",
  "https": "http://127.0.0.1:11080",
}

r=requests.get(url,proxies=proxies)
data=r.text

for link,t in set(re.findall(r'(https:[^\s]*?(jpg|png|gif))',str(data))):
    print(link,t)
    try:
        # urllib.request.urlretrieve(link,saveFile(link))
        requests.get(link,proxies=proxies)
    except:
        print(sys.exc_info())
        print('失败')
