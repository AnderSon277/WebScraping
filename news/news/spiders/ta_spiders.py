import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_ta'
    allowed_domains = ['tctelevision.com/']
    start_urls = [
    'http://www.teleamazonas.com/noticiero-24-horas/noticias-nacionales/',
    'http://www.teleamazonas.com/noticiero-24-horas/noticias-internacionales/',
    'http://www.teleamazonas.com/noticiero-24-horas/los-desayunos/',
    'http://www.teleamazonas.com/actualidad/insolito/',
    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="bp-head"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('h2/a/text()').extract()[0]
            item['url']=headline.xpath('h2/a/@href').extract()[0]
            yield item
