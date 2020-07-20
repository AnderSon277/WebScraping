import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_ev'
    allowed_domains = ['ecuavisa.com//']
    start_urls = [
    'https://www.ecuavisa.com/noticias/nacional',
    'https://www.ecuavisa.com/noticias/internacional',
    'https://www.ecuavisa.com/noticias/economia',
    'https://www.ecuavisa.com/noticias/politica',
    'https://www.ecuavisa.com/estadio/nacional',
    'https://www.ecuavisa.com/estadio/internacional',
    'https://www.ecuavisa.com/estadio/masdeportes',
    'https://www.ecuavisa.com/entretenimiento/nacional',
    'https://www.ecuavisa.com/entretenimiento/internacional',
    'https://www.ecuavisa.com/tendencias/tecnologia',
    'https://www.ecuavisa.com/tendencias/ciencia',
    'https://www.ecuavisa.com/tendencias/medicina',
    'https://www.ecuavisa.com/tendencias/redes',
    'https://www.ecuavisa.com/tendencias/curiosidades'
    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="views-field views-field-title"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('span/a/text()').extract()[0]
            item['url']=headline.xpath('span/a/@href').extract()[0]
            yield item