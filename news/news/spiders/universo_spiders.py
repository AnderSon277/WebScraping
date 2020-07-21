import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_universo'
    allowed_domains = ['www.eluniverso.com/']
    start_urls = [
    'https://www.eluniverso.com/politica',
    'https://www.eluniverso.com/economia',
    'https://www.eluniverso.com/internacional',
    'https://www.eluniverso.com/ecuador',
    'https://www.eluniverso.com/intercultural',
    'https://www.eluniverso.com/seguridad',
    'https://www.eluniverso.com/ecologia',
    'https://www.eluniverso.com/informes',
    'https://www.eluniverso.com/guayaquil',
    'https://www.eluniverso.com/comunidad',
    'https://www.eluniverso.com/samborondon',
    'https://www.eluniverso.com/urdesa-ceibos',
    'https://www.eluniverso.com/via-costa',
    'https://www.eluniverso.com/peninsula',
    'https://www.eluniverso.com/deportes',
    'https://www.eluniverso.com/futbol'
    'https://www.eluniverso.com/campeonato-ecuatoriano',
    'https://www.eluniverso.com/columnistas-deportes',
    'https://www.eluniverso.com/futbol-internacional',
    'https://www.eluniverso.com/ecuatorianos-exterior',
    'https://www.eluniverso.com/otros-deportes',
    'https://www.eluniverso.com/memorias-deportivas',
    'https://www.eluniverso.com/entretenimiento',
    'https://www.eluniverso.com/cine',
    'https://www.eluniverso.com/television',
    'https://www.eluniverso.com/videojuegos',
    'https://www.eluniverso.com/gastronomia',
    'https://www.eluniverso.com/cultura',
    'https://www.eluniverso.com/musica',
    'https://www.eluniverso.com/teatro',
    'https://www.eluniverso.com/gente',
    'https://www.eluniverso.com/redes-sociales',
    'https://www.eluniverso.com/turismo-local',
    'https://www.eluniverso.com/libros',
    'https://www.eluniverso.com/compras',
    'https://www.eluniverso.com/columnistas-vida',
    'https://www.eluniverso.com/motores',
    'https://www.eluniverso.com/larevista',
    'https://www.eluniverso.com/tecnologia',
    'https://www.eluniverso.com/cuerpo-alma',
    'https://www.eluniverso.com/columnistas-larevista',
    'https://www.eluniverso.com/el-especialista',
    'https://www.eluniverso.com/espectaculos',
    'https://www.eluniverso.com/orientacion',
    'https://www.eluniverso.com/sociedad',
    'https://www.eluniverso.com/moda',
    'https://www.eluniverso.com/diseno',
    'https://www.eluniverso.com/cocina',
    'https://www.eluniverso.com/salud',
    'https://www.eluniverso.com/destinos',
    'https://www.eluniverso.com/arte'
    ]

    def parse(self, response):
        headlines=Selector(response).xpath('//div[@class="summary views-fieldset"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('h2/a/text()').extract()[0]
            item['url']='www.eluniverso.com'+headline.xpath('h2/a/@href').extract()[0]
            yield item