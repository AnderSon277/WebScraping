import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['tctelevision.com/']
    start_urls = [
    'https://www.tctelevision.com/programa/el-noticiero',
    'https://www.tctelevision.com/cronica'
    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="qt-itemcontents"]')
        cronics=Selector(response).xpath('//div[@class="qt-part-archive-item qt-part-archive-item-inline"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('h5/a/text()').extract()[0]
            item['url']=headline.xpath('h5/a/@href').extract()[0]
            yield item
        for cronic in cronics:
            item['title']=cronic.xpath('h6/a/text()').extract()[0]
            item['url']=cronic.xpath('h6/a/@href').extract()[0]
            yield item