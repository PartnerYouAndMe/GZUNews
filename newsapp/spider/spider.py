import requests

class News:

    def __init__(self):
        self.url='http://lib.gzu.edu.cn/1470/list.htm'
    
    def getData(self,data,headers):
        self.html = requests.request('GET',self.url,data=data,headers=headers)
        print(self.html.json())

if __name__ == "__main__":
    news=News()
    data={
        'siteID':38,
        'type':2,
        'columnID':1470
    }
    headers={
        'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=D4C1447FE5B60E3B5A486F6F41DA2E61',
        'Host': 'lib.gzu.edu.cn',
        'Referer': 'http://lib.gzu.edu.cn/1470/list.htm',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    news.getData(data,headers)