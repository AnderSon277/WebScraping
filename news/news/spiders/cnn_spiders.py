import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_cnn'
    allowed_domains = ['cnnespanol.cnn.com/']
    start_urls = [
    'https://cnnespanol.cnn.com/',
    'https://cnnespanol.cnn.com/seccion/mundo/',
    'https://cnnespanol.cnn.com/seccion/latinoamerica/',
    'https://cnnespanol.cnn.com/seccion/estados-unidos/',
    'https://cnnespanol.cnn.com/seccion/mundo/',
    'https://cnnespanol.cnn.com/seccion/economia-y-negocios/',
    'https://cnnespanol.cnn.com/seccion/entretenimiento/',
    'https://cnnespanol.cnn.com/seccion/tecnologia/',
    'https://cnnespanol.cnn.com/seccion/deportes/',
    'https://cnnespanol.cnn.com/seccion/viajes-y-turismo/',
    'https://cnnespanol.cnn.com/seccion/salud/',
    'https://cnnespanol.cnn.com/seccion/estilo/',
    'https://cnnespanol.cnn.com/seccion/opinion/',
    'https://cnnespanol.cnn.com/radio/',
    'https://cnnespanol.cnn.com/especiales/',
    'https://cnnespanol.cnn.com/category/africa/',
    'https://cnnespanol.cnn.com/category/asia/',
    'https://cnnespanol.cnn.com/category/espana/',
    'https://cnnespanol.cnn.com/category/europa/',
    'https://cnnespanol.cnn.com/category/medio-oriente/'
    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//h2[@class="news__title"]')
        #titles=Selector(response).xpath('//div[@class="qt-part-archive-item qt-part-archive-item-inline"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('a/text()').extract()[0]
            item['url']=headline.xpath('a/@href').extract()[0]
            yield item