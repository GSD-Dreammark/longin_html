# 知乎首页
import scrapy
from lxml import etree
import redis
from scrapy.http import Request
class test(scrapy.Spider):
    name = "test" #要调用的名字
    allowed_domains = [] #分一个域
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        url="https://www.zhihu.com/#signin"
        yield Request(url,headers=self.headers)
    def parse(self, response):
        # print(response.body.decode('utf-8'))
        xsrf = response.xpath('//input[@name="_xsrf"]/@value').extract()[0]
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
                                   formdata={'_xsrf':xsrf, 'account': '18447052587','password':'917687690','captcha':'','captcha_type':captcha_type},
                                   callback=self.logged_in)]

    def logged_in(self, response):
        print('++++++++++++++++++++')
        print(response.body.decode('utf-8'))

