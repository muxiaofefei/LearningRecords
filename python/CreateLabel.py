#创建标签

import sys
import io
from urllib import request
import re
from bs4 import BeautifulSoup
from xpinyin import Pinyin
import requests


#浏览器登录后得到的cookie，也就是刚才复制的字符串
# cookie_str = input("请输入cookie：")
cookie_str = '_csrf=08fe0d09727425d311f27f3b795247ad49c39c418d01ba3ee91b2bdc912d4345a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22L%F7%7C%07%DE%07M%C6%A3%D7%EC%8An%90q%CC%1F%FE%DD%B4%C2f%BE%B7%EB%05%FBu%7C%DE%AE%FF%22%3B%7D; CONTAINERID=3f0b3b6fd10f0743fccfc22ba546bd2aab77c443f7f1f42e9f524b3f35cb1a53; RMTSESSION_FRONTEND=da2a71735933096ac3ae8cd30116a05f; _identity=4c541d71e7e22e55286932bd71ce5bde4e76a304b7e12c99ec0f773b02d83299a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A43%3A%22%5B%22admin%40tzxinwen%22%2C%22admin%40tzxinwen%22%2C2592000%5D%22%3B%7D'

scrf = 'odqmmeWYhMypl3ZtBTdvib1ctN1OiL5ZCDRTPEICzvHtLdqeO5_JCgpAmudrpx5FoqJpaYzuAO7jMahJPtxgDg=='


# cookeis设置
jar = requests.cookies.RequestsCookieJar()
cookiestr = cookie_str.split(';')
for cookies in cookiestr:
	cookiesplit = cookies.split('=')
	jar.set(cookiesplit[0],cookiesplit[1])


# 标签内容
dataval=[
	'姜堰要闻',
	'部门动态',
	'区镇动态',
	'社会民生',
	'图片新闻',
	'视频新闻',
	'今日姜堰',
	'读者社区',
	'消费广场',
	'娱乐休闲',
	'健康养生',
	'公示公告',
	'领导报道集',
	'图片推荐',
	'热门新闻',
	'阅读推荐',
	'相关文章',
]




# 创建标签

# 测试
# url = 'http://mp.rmt.test.routeryuncs.com/config/tags/create'

# 正式
url = 'http://mp.tmtsp.com/config/tags/create'

for datastr in dataval:
	data = {
	'_csrf':scrf,
	'Tags[name]':datastr,
	'Tags[class]':'group',
	'Tags[state]':'1',
	'Tags[sort]':'',
	}
	r = requests.post(url,data,cookies=jar)
print("创建完成")




# 删除停用标签


# bqyurl ='http://mp.rmt.test.routeryuncs.com/config/tags/index'
# r = requests.get(bqyurl,cookies=jar)
# soup = BeautifulSoup(r.text)
# stoplab = soup.find_all("div", class_="col-md-4")
# stoplab_a = stoplab[0].find_all('a')
# for stpa in stoplab_a:
# 	stpahref = stpa.get('href')
# 	id = stpahref.split('?')
# 	durl = 'http://mp.rmt.test.routeryuncs.com/config/tags/delete'+'?'+id[1]
# 	r = requests.get(durl,cookies=jar)
# print('删除完成')


