import requests
from bs4 import BeautifulSoup

url=r'http://lib.gzu.edu.cn/1470/list'

headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'max-age=0',
    'Connection': 'close',
    # 'Cookie': 'JSESSIONID=3EE008BC56D9C625354BADE4BF34F4C6',
    # 'Host': 'lib.gzu.edu.cn',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
}
s=url+str(17)+'.psp'

import time
b=False
while(b==False):
    
    try:
        res=requests.request('GET',s,headers=headers)
        b=True
    except:
        print('访问拒绝，休息5s')
        time.sleep(5)
        continue


res.encoding='utf-8'

links=[]
soup=BeautifulSoup(res.text,'html.parser')
for all in soup.select('#wp_news_w2 table'):
    link=all.select('a')[0]['href']
    links.append(link)

import pymysql
pageUrl=r'http://lib.gzu.edu.cn'
db=pymysql.connect('localhost','root','123456','news')
cursor=db.cursor()
newsID=240
for i in links:   #第一篇文章不知道为什么有两个，所以从1开始,有14*28个链接
    newUrl2=pageUrl+i
    print(newUrl2)
    res=requests.request('GET',newUrl2)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    title=soup.select('.Article_Title')[0].text      #存标题
    publicTime=soup.select('.Article_PublishDate')[0].text    #存发布时间
    publicContent=soup.select('.Article_Content')[0].text    #存内容
    visitCount=soup.select('.WP_VisitCount')[0].text    #存点击次数
    print(title,end=' ')
    #存到数据库中
    newsID += 1
    insert="insert into newsapp_newsitem \
        values('"+str(newsID)+"','"+title+"','"+publicTime+"','"+publicContent+"','"+visitCount+"');"
    cursor.execute(insert)
    print(newsID) 
db.commit()