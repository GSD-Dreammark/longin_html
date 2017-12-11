# 模拟登陆 爬自己的页面
import scrapy
import redis
from lxml import etree
from scrapy.http import Request
# 把起点首页的所有列表
class login_spider(scrapy.Spider):
    name = "login_spider" #要调用的名字
    allowed_domains = [] #分一个域
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        url = "http://127.0.0.1:8000/index/loginHtml/"
        return [scrapy.FormRequest(url,callback=self.post_login,headers=self.headers)]
    def post_login(self, response):
            print('Preparing login')
            # 一定要注意allowed_domains 很关键，只要是callback 就一定回去allowed_domains去看是否匹配
            # 主要是scrapy.FormRequest() 可以加浏览器头+和cookie 和Request的参数差不多
            selector = etree.HTML(response.body.decode('utf-8'))
            links = selector.xpath('//form/input[@name="csrfmiddlewaretoken"]/@value')
            for link in links:
                csrfmiddlewaretoken = link
                print(link)
            return [scrapy.FormRequest("http://127.0.0.1:8000/index/login/",
                                       formdata={'csrfmiddlewaretoken': csrfmiddlewaretoken, 'email': 'aa',
                                                 'pwd': 'aa'},
                                       callback=self.logged_in,headers=self.headers)]
    def logged_in(self, response):
        print('))0000)(((((')
        print(response.body.decode('utf-8'))

    def parse(self, response):
        print('___________')
        print(response.body)
