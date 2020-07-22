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
    'http://www.teleamazonas.com/hora25ec/',
    'http://www.teleamazonas.com/actualidad/',
    'http://www.teleamazonas.com/actualidad/insolito/',
    'http://www.teleamazonas.com/actualidad/dia-a-dia/',
    'http://www.teleamazonas.com/actualidad/ciencia-y-tecnologia/',
    'http://www.teleamazonas.com/actualidad/salud-en-linea/',
    'http://www.teleamazonas.com/farandula/en-corto/',
    'http://www.teleamazonas.com/deportes/'
    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="bp-head"]')
        titles=Selector(response).xpath('//div[@class="post-title"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('h2/a/text()').extract()[0]
            item['url']=headline.xpath('h2/a/@href').extract()[0]
            yield item
        for title in titles:
            item['title']=title.xpath('h2/a/text()').extract()[0]
            item['url']=title.xpath('h2/a/@href').extract()[0]
            yield item