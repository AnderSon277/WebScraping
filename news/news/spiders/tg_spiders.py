import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_tg'
    allowed_domains = ['eltelegrafo.com.ec']
    start_urls = [
    'https://www.eltelegrafo.com.ec/contenido/categoria/1/politica',
    'https://www.eltelegrafo.com.ec/contenido/categoria/1/pedro-el-economista',
    'https://www.eltelegrafo.com.ec/contenido/categoria/1/futbol-internacional',
    'https://www.eltelegrafo.com.ec/contenido/categoria/6/sociedad',
    'https://www.eltelegrafo.com.ec/contenido/categoria/1/tecnologia'
    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="col-xs-8"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('h2/a/text()').extract()[0]
            item['url']=headline.xpath('h2/a/@href').extract()[0]
            yield item
