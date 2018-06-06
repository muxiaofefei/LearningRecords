# 自动抓取栏目key值
#只抓取特定的客户端的key

import sys
import io
from urllib import request
import re
from bs4 import BeautifulSoup
from xpinyin import Pinyin
import requests


# username = 'admin@jrlx.com'
# password = '59002e94532d7'
# state = '0'

state = input("正式输1，测试输0：")
username = input("请输入账号：")
password = input("请输入密码：")
cstkey = input("请输入客户端的key值：")

if state == '1':
    loginUrl = 'http://mp.tmtsp.com'
else:
    loginUrl = 'http://mp.rmt.test.routeryuncs.com'

agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    'User-Agent': agent
}

s = requests.Session()
r=s.get(loginUrl,allow_redirects=True, headers=headers)
html = r.text
# print (loginUrl)

pattern = r'name="_csrf" value="(.*?)"'
_csrf = re.findall(pattern,html)

datas={
'_csrf':_csrf[0],
'LoginForm[username]':username,
'LoginForm[password]':password,
'remember':'on',
}

if state == '1':
    zloginUrl = 'http://mp.tmtsp.com/common/safe/login'
else:
    zloginUrl = 'http://mp.rmt.test.routeryuncs.com/common/safe/login'

r = s.post(zloginUrl, data=datas, allow_redirects=True, headers=headers)
# print (r.text)

url = loginUrl+'/client/client-config'
r = s.get(url,headers=headers)
# print (r.text)

html = r.text
pattern = r'class="item" data-key="(.*?)"'
data_key = re.findall(pattern,html)
# print(data_key)

url = loginUrl+'/client/manage/index?id='+cstkey
r = s.get(url, headers=headers)
html = r.text
# print (html)
pattern = r'class = "btn btn-primary br2 btn-xs fs12" href = "(.*?)"'
curl = re.findall(pattern, html)
# print (curl)
for colm in curl:

    url = loginUrl+''+colm
    r = s.get(url, headers=headers)

    htmlcont = r.text

    # 解析网页
    soup = BeautifulSoup(htmlcont)

    # 中文转拼音库
    p = Pinyin()

    tr = soup.find_all('tr')

    i = 0

    print ('==================================================')

    for t in tr:
        if i == 0:
            i += 1
            continue
        td = t.find_all('td')
        print('"' + p.get_initials(td[1].contents[0], u'') + '"' + '=>' + '"' + t.get(
            'data-tb-id') + '"' + ',' + '    ' + '//' + td[1].contents[0])
