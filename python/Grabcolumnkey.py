# 自动抓取栏目key值

import sys
import io
from urllib import request
import re
from bs4 import BeautifulSoup
from xpinyin import Pinyin

# cookie数据
cookie_str = r'_csrf=aa1943b556d809619e55eaabb2a123c575742288f190b16263f7e74a70dfc1f9a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22d%B4%F5b%2B%1F%B0BN%19gt%99%09M%B4%ACzL%BFH+%D7%836%DC%8FQ%A7%88%D3%D1%22%3B%7D; CONTAINERID=20f731794e516105f4e374d8c3fa8215782133e2ce2ffe1450374d1317ca3f0e; RMTSESSION_FRONTEND=41cf2a16b85c4a1ab13f01a8bf8600b2; _identity=fefc94305d7bc3d4e9737b3018249b747cd5a5695adec09522dd0921a9004876a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A51%3A%22%5B%22admin%40langxi.local%22%2C%22admin%40langxi.local%22%2C2592000%5D%22%3B%7D'

# 访问在地址
url = 'http://mp.rmt.test.routeryuncs.com/client/vchannel?module_id=5ac4295575c3a414008b4567'

req = request.Request(url)
#设置cookie
req.add_header('cookie', cookie_str)
#设置请求头
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

resp = request.urlopen(req)

htmlcont = resp.read().decode('utf-8')

# 解析网页
soup = BeautifulSoup(htmlcont)

# 中文转拼音库
p = Pinyin()

tr = soup.find_all('tr')

i=0
for t in tr:
    if i == 0:	
        i += 1
        continue
    td = t.find_all('td')
    print('"'+p.get_initials(td[1].contents[0], u'')+'"'+'=>'+'"'+t.get('data-tb-id')+'"'+','+'    '+'//'+td[1].contents[0])