import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_ev'
    allowed_domains = ['ecuavisa.com//']
    start_urls = [
    'https://www.ecuavisa.com/noticias/nacional',
    'https://www.ecuavisa.com/historico/noticias/nacional',
    'https://www.ecuavisa.com/noticias/internacional',
    'https://www.ecuavisa.com/historico/noticias/internacional',
    'https://www.ecuavisa.com/noticias/economia',
    'https://www.ecuavisa.com/historico/noticias/economia',
    'https://www.ecuavisa.com/noticias/politica',
    'https://www.ecuavisa.com/historico/noticias/politica',
    'https://www.ecuavisa.com/estadio/nacional',
    'https://www.ecuavisa.com/historico/estadio/nacional',
    'https://www.ecuavisa.com/estadio/internacional',
    'https://www.ecuavisa.com/historico/estadio/internacional',
    'https://www.ecuavisa.com/estadio/masdeportes',
    'https://www.ecuavisa.com/historico/estadio/masdeportes',
    'https://www.ecuavisa.com/entretenimiento/nacional',
    'https://www.ecuavisa.com/entretenimiento/internacional',
    'https://www.ecuavisa.com/historico/entretenimiento/internacional',
    'https://www.ecuavisa.com/tendencias/tecnologia',
    'https://www.ecuavisa.com/historico/tendencias/tecnologia',
    'https://www.ecuavisa.com/tendencias/ciencia',
    'https://www.ecuavisa.com/historico/tendencias/ciencia',
    'https://www.ecuavisa.com/tendencias/medicina',
    'https://www.ecuavisa.com/historico/tendencias/medicina',
    'https://www.ecuavisa.com/tendencias/redes',
    'https://www.ecuavisa.com/historico/tendencias/redes',
    'https://www.ecuavisa.com/tendencias/curiosidades',
    'https://www.ecuavisa.com/historico/tendencias/curiosidades'
    ]
    #Add all pages
    for i in range(1,3):
        start_urls.append('https://www.ecuavisa.com/historico/noticias/nacional?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/noticias/internacional?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/noticias/economia?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/noticias/politica?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/estadio/nacional?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/estadio/internacional?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/estadio/masdeportes?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/entretenimiento/internacional?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/tendencias/tecnologia?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/tendencias/ciencia?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/tendencias/medicina?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/tendencias/redes?page='+str(i))
        start_urls.append('https://www.ecuavisa.com/historico/tendencias/curiosidades?page='+str(i))


    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="views-field views-field-title"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('span/a/text()').extract()[0]
            item['url']='https://www.ecuavisa.com'+headline.xpath('span/a/@href').extract()[0]
            yield item