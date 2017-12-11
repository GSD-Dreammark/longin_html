# 爬一个图片
import scrapy
from scrapy.http import Request
class login_douban(scrapy.Spider):
    name = "spider_image" #要调用的名字
    allowed_domains = [] #分一个域
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        url="http://img.sc115.com/wm/xqx/pic/1501gsuvdec4mxq.jpg"
        # 好像没cookie 不能访问
        yield Request(url)
    def parse(self, response):
        self.dimage(response)
    def dimage(self,response):
        pic = response.body
        # 文件必须先存在，不会自动创建，如果不存在会显示在cmd窗口中
        imgPath = 's.jpg'
        fb = open(imgPath, 'wb')
        fb.write(pic)
        fb.close()
        print("success")