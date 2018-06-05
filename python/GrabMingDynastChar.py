# 抓取某网站-明朝著名人物
# encoding:utf-8
import requests
from bs4 import BeautifulSoup
import re
import codecs
import webbrowser

head = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}
GEN_HTML = 'MingDynasty.html'
fout = codecs.open(GEN_HTML, 'w', encoding='utf-8')
fout.write("<html>")
fout.write("<head><meta charset='utf-8'/></head>")
fout.write("<body>")
fout.write("<table>")


for num in range(1,21):
    if(num == 1):
            url = 'http://ren.bytravel.cn/Celebrity/cd_mingchao.html'
    else:
        num = num - 1
        url = 'http://ren.bytravel.cn/Celebrity/cd_mingchao{mynum}.html' \
            .format(mynum=num)

    r = requests.get(url,headers = head)
    r.encoding = 'GBK'

    soup = BeautifulSoup(r.text)
    list = soup.find_all(class_='blue14b')

    for li in list:
        fout.write("<tr>")
        fout.write("<td><a href='http://ren.bytravel.cn%s'>%s</a></td>" % (li.get('href'),li.text))
        fout.write("</tr>")


fout.write("</table>")
fout.write("</body>")
fout.write("</html>")
fout.close()

print('完成')

webbrowser.open(GEN_HTML,new = 1)
