import scrapy
from scrapy.http import Request
from test1.items import NewHouse, OldHouse  # 从items.py中引入MyItem对象


class NewSpider(scrapy.Spider):
    name = "new" #爬虫的名字是new
    allowed_domains = ["bj.fang.lianjia.com"] #允许爬取的网站域名
    custom_settings = {
        'ITEM_PIPELINES' : {'test1.pipelines.NewPipeline' : 300},
    }
    start_urls = ["https://bj.fang.lianjia.com/loupan/pg3/"]
    pagenum = 3
    #初始URL，即爬虫爬取的第一个URL
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = NewHouse() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[@class="resblock-list-container clearfix"]/ul[@class="resblock-list-wrapper"]/li[*]/div[@class="resblock-desc-wrapper"]'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            item['name'] = each.xpath('div[@class="resblock-name"]/a/text()').extract()
            item['house_type'] = each.xpath('div[@class="resblock-name"]/span[@class="resblock-type"]/text()').extract()
            item['position'] = each.xpath('div[@class="resblock-location"]/a/text()').extract()
            item['room_type'] = each.xpath('a[@class="resblock-room"]/span/text()').extract()
            item['area'] = each.xpath('div[@class="resblock-area"]/span/text()').extract()
            item['unit_price'] = each.xpath('div[@class="resblock-price"]/div[@class="main-price"]/span[@class="number"]/text()').extract()
            item['total_price'] = each.xpath('div[@class="resblock-price"]/div[@class="second"]/text()').extract()
            item['unit_price'][0] += "元/平"
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum < 8:
            url = f"https://bj.fang.lianjia.com/loupan/pg{self.pagenum}/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)
            
class OldSpider(scrapy.Spider):
    name = "old" #爬虫的名字是new
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    custom_settings = {
        'ITEM_PIPELINES' : {'test1.pipelines.OldPipeline' : 300},
    }
    start_urls = ["https://bj.lianjia.com/ershoufang/pg3/"]
    pagenum = 3
    #初始URL，即爬虫爬取的第一个URL
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = OldHouse() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[@class="content "]/div[@class="leftContent"]/ul[@class="sellListContent"]/li[*]/div[@class="info clear"]'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            item['cell_name'] = each.xpath('div[@class="flood"]/div[@class="positionInfo"]/a[1]/text()').extract()
            item['position'] = each.xpath('div[@class="flood"]/div[@class="positionInfo"]/a[2]/text()').extract()
            item['room_type'] = each.xpath('div[@class="address"]/div/text()').extract()
            item['unit_price'] = each.xpath('div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()').extract()
            item['total_price'] = each.xpath('div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/span/text()').extract()
            item['total_price'][0] += "万"
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum < 8:
            url = f"https://bj.lianjia.com/ershoufang/pg{self.pagenum}/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)
