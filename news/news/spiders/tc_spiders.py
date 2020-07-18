import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['tctelevision.com/']
    start_urls = [
    'https://www.tctelevision.com/programa/el-noticiero',
    'https://www.tctelevision.com/cronica',
    'https://www.tctelevision.com/ciencia-tecnologia',
    'https://www.tctelevision.com/comunidad',
    'https://www.tctelevision.com/politica',
    'https://www.tctelevision.com/tendencias',
    'https://www.tctelevision.com/deportes',
    'https://www.tctelevision.com/entretenimiento',
    'https://www.tctelevision.com/tags/coronavirus'
    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="qt-itemcontents"]')
        titles=Selector(response).xpath('//div[@class="qt-part-archive-item qt-part-archive-item-inline"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('h5/a/text()').extract()[0]
            item['url']=headline.xpath('h5/a/@href').extract()[0]
            yield item
        for title in titles:
            item['title']=title.xpath('h6/a/text()').extract()[0]
            item['url']=title.xpath('h6/a/@href').extract()[0]
            yield item