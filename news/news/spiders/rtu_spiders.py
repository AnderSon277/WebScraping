import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_bbc'
    allowed_domains = ['www.bbc.com/']
    start_urls = [
    'https://www.bbc.com/mundo',

    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//h3[@class="Headline-sc-1dvfmi3-3 dnWhDh"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('a/text()').extract()[0]
            item['url']='https://www.bbc.com/'+headline.xpath('a/@href').extract()[0]
            yield item