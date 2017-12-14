# 知乎首页
import scrapy
from lxml import etree
import redis
from scrapy.http import Request
class test(scrapy.Spider):
    name = "test" #要调用的名字
    allowed_domains = [] #分一个域
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
        #'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    headers1 = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    headers2 = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }
    def start_requests(self):
        url="https://www.zhihu.com/#signin"
        yield Request(url,headers=self.headers2,callback=self.parse)
    def parse(self, response):
        print('++++++++++++++++')
        xsrf = response.xpath('//input[@name="_xsrf"]/@value').extract()[0]
        print(xsrf)
        print('++++++++!')
        # 验证码的链接是后添加上去的
        # imgsrc=response.xpath('//img[@class="Captcha-image"]/@src').extract()[0]
        # captcha_type=response.xpath('//input[@name="captcha_type"]/@value').extract()[0]
        # print(xsrf)
        # print(imgsrc)
        # print(captcha_type)
        # 这个值好像是图片对应的值
        # captcha=response.xpath('//input[@name="captcha"]/@value').extract()[0]
        # print(captcha)
        # 一定要注意allowed_domains 很关键，只要是callback 就一定回去allowed_domains去看是否匹配
        # ++++++++++++++++++++++++++
        # 登录爬取 1.首先是要找到form提交的页面
        #          2.找到所有可能提交的数据
        #          3.验证码问题
        return [scrapy.FormRequest("https://www.zhihu.com/#signin",
                                   formdata={'_xsrf':xsrf, 'account': '18447052587','password':'917687690','captcha_type':'cn'},
                                   callback=self.logged_in,headers=self.headers2)]

    def logged_in(self, response):
        print('++++++++++++++++++++')
        print(response.body.decode('utf-8'))

