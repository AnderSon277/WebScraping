import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_tg'
    allowed_domains = ['news.google.com']
    start_urls = [
    'https://news.google.com/',
    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="xrnccd F6Welf R7GTQ keNKEd j7vNaf"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('a/text()').extract()[0]
            item['url']=headline.xpath('a/@href').extract()[0]
            yield item
