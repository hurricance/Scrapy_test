import scrapy
from scrapy.crawler import CrawlerProcess

from test1.spiders.spider import NewSpider, OldSpider

process = CrawlerProcess()
process.crawl(NewSpider)
process.crawl(OldSpider)
process.start()
