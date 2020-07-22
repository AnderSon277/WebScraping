import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_rts'
    allowed_domains = ['http://www.rts.com.ec/']
    start_urls = [
    'http://www.rts.com.ec/noticias/novelas-18111',
    'http://www.rts.com.ec/noticias/actualidad-1',
    'http://www.rts.com.ec/noticias/deportes-3',
    'http://www.rts.com.ec/noticias/espectaculos-2',
    'http://www.rts.com.ec/noticias/tendencias-18110'
    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="col-12 col-sm-8 col-md-8 col-lg-8 col-xl-8 pd-left-ultimas-noticias"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('a/h2/text()').extract()[0]
            item['url']=headline.xpath('a/@href').extract()[0]
            yield item