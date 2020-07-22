import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_ecuTV'
    allowed_domains = ['www.ecuadortv.ec/']
    start_urls = [
    'https://www.ecuadortv.ec/actualidad'
    ]
    #Add All pages
    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="col-12"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('a/text()').extract()[0]
            item['url']='https://www.ecuadortv.ec'+headline.xpath('a/@href').extract()[0]
            yield item