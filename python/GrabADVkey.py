# 自动抓取广告位key值

import sys
import io
from urllib import request
import re
from bs4 import BeautifulSoup
from xpinyin import Pinyin


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = input("请输入cookie：")
# '_csrf=ce8590669b7fe9bfadc894f3e134fa221ebdf945905bd586a81e8be82062f3a6a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22%1F%B0%86%8E.1%EC%A4%8B2%AF%C7F%08oh%F8%2F%CB%C0%89j%EE%28vP%16%7D%C3%B7%EE%B1%22%3B%7D; CONTAINERID=20f731794e516105f4e374d8c3fa8215782133e2ce2ffe1450374d1317ca3f0e; RMTSESSION_FRONTEND=49e637e2df6cbe6ca36d1ae6aeb0e995; _identity=94d7171277d110109efe0460aef85dea4d9fb68094288290d82e1f9990e9e32da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A63%3A%22%5B%225ad46bc9e27dab13008b4567%22%2C%225ad46bc9e27dab13008b4567%22%2C2592000%5D%22%3B%7D'

#登录后才能访问的网页
url = input("请输入网址：")
# 'http://mp.rmt.test.routeryuncs.com/plugin/ad-manage'

req = request.Request(url)
#设置cookie
req.add_header('cookie', cookie_str)
#设置请求头
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

resp = request.urlopen(req)

htmlcont = resp.read().decode('utf-8')

soup = BeautifulSoup(htmlcont)
# print(soup.prettify())

p = Pinyin()

tr = soup.find_all('tr')
# print(tr[1])

i=0
for t in tr:
    if i == 0:	
        i += 1
        continue
    td = t.find_all('td')
    a = td[5].find('a').get('href')

    id = a.split('=')
    print('"ADV_'+p.get_initials(td[2].contents[0].strip(), u'')+'"'+'=>'+'"'+id[1]+'"'+','+'    '+'//'+td[2].contents[0].strip())

