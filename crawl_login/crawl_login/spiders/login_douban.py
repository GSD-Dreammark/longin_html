# 知乎首页
import scrapy
import requests
from urllib.request import Request as R
from urllib.request import urlopen
from scrapy.http.cookies import CookieJar
from scrapy.http import Request
class login_douban(scrapy.Spider):
    name = "login_douban" #要调用的名字
    allowed_domains = [] #分一个域
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    head = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    start_urls = [
       "https://www.douban.com/"
       #  'https://accounts.douban.com/login'
    ]
    #好像没cookie 不能访问
    def start_requests(self):
        for url in self.start_urls:
            # 好像没cookie 不能访问
            cookie_jar = CookieJar()
            yield Request(url,meta={'cookiejar':cookie_jar},headers=self.head,callback=self.login_in)
    def login_in(self, response):
        print("success")
        captcha_id=response.xpath('//div[@class="captcha_block"]/input[@name="captcha-id"]/@value').extract()[0]
        image_src=response.xpath('//img[@id="captcha_image"]/@src').extract()[0]
        self.dimage(image_src)
        captcha = input("请输入验证码：")
        print('++++++++++++++++++++')
        print('+++++++++++++++++++')
        return [scrapy.FormRequest("https://accounts.douban.com/login",
                                   formdata={'source':'index_nav','redir': 'https://www.douban.com/','form_email':'15532108480','form_password':'228yuhailong','captcha-solution':captcha,'captcha-id':captcha_id},
                                   meta={'cookiejar': response.meta['cookiejar']},
                                   callback=self.parse,headers=self.head)]

    def parse(self, response):
        print(response.body.decode('utf-8'))
    def dimage(self,url):
        req_timeout = 5
        req = R(url=url)
        f = urlopen(req, None, req_timeout)
        pic = f.read()
        # 文件必须先存在，不会自动创建，如果不存在会显示在cmd窗口中
        imgPath = 's.jpg'
        fb = open(imgPath, 'wb')
        fb.write(pic)
        fb.close()