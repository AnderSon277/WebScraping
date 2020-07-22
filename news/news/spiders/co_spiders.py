import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_co'
    allowed_domains = ['elcomercio.com']
    start_urls = [
    'https://www.elcomercio.com/actualidad',
    'https://www.elcomercio.com/venezolanos-en-ecuador',
    'https://www.elcomercio.com/periodistas-en-la-frontera-norte',
    'https://www.elcomercio.com/deportes',
    'https://www.elcomercio.com/data',
    'https://www.elcomercio.com/tendencias',
    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="article articulo-grande"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('a/text()').extract()[0]
            item['url']=headline.xpath('a/@href').extract()[0]
            yield item
