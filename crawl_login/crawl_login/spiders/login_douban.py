# 知乎首页
import scrapy
import requests
import http.cookiejar
from scrapy.http import Request
class login_douban(scrapy.Spider):
    name = "login_douban" #要调用的名字
    allowed_domains = [] #分一个域
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    #好像没cookie 不能访问
    cj = http.cookiejar.CookieJar()
    cookie=requests.cookies.RequestsCookieJar(cj)
    def start_requests(self):
        url="https://www.douban.com/"
        # 好像没cookie 不能访问
        # cj = http.cookiejar.CookieJar()
        # cookie = requests.cookies.RequestsCookieJar(cj)
        # print(cookie)
        yield Request(url,meta={'cookiejar':1},headers=self.headers,callback=self.login_in)
    def login_in(self, response):
        print("success")
        # print(response.body.decode('utf-8'))
        # selector = etree.HTML(response.url)
        # find hidden value
        # captcha_ids = selector.xpath('//input[@name="captcha-id"]/@value');
        # for link in captcha_ids:
        #     captcha_id = link
        print('+++++++++++++++++++')
        return [scrapy.FormRequest("https://www.douban.com/accounts/login",
                                   formdata={'source':'index_nav','redir':'https://www.douban.com/','form_email':'15532108480','form_password':'228yuhailong','captcha_id':""},
                                   meta={'cookiejar': response.meta['cookiejar']},
                                   callback=self.parse,headers=self.headers)]

    def parse(self, response):
        print('++++++++++++++++++++')
        print(response.body.decode('utf-8'))