import scrapy
from scrapy import Spider
from scrapy import Selector

from news.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news_BBC'
    i=1
    allowed_domains = ['www.bbc.com/']
    start_urls = [
        'https://www.bbc.com/mundo/topics/ckdxnw959n7t',#ciencia
        'https://www.bbc.com/mundo/topics/c7zp57yyz25t',#america latina
        'https://www.bbc.com/mundo/topics/c06gq9v4xp3t',#economia
        'https://www.bbc.com/mundo/topics/cyx5krnw38vt',#tecnologia
        'https://www.bbc.com/mundo/topics/cpzd498zkxgt',#salud
        'https://www.bbc.com/mundo/topics/c2dwq9zyv4yt',#sociendad y cultura
        'https://www.bbc.com/mundo/topics/cr50y726329t',#deportes
    ]
    #Add All pages
    for i in range(2,101):
        start_urls.append('https://www.bbc.com/mundo/topics/ckdxnw959n7t/page/'+str(i))
        start_urls.append('https://www.bbc.com/mundo/topics/c7zp57yyz25t/page/'+str(i))
        start_urls.append('https://www.bbc.com/mundo/topics/c06gq9v4xp3t/page/'+str(i))
        start_urls.append('https://www.bbc.com/mundo/topics/cpzd498zkxgt/page/'+str(i))
        start_urls.append('https://www.bbc.com/mundo/topics/c2dwq9zyv4yt/page/'+str(i))
    for i in range(2,72):
        start_urls.append('https://www.bbc.com/mundo/topics/cyx5krnw38vt/page/'+str(i))
    for i in range(2,23):
        start_urls.append('https://www.bbc.com/mundo/topics/cr50y726329t/page/'+str(i))

    def parse(self, response):
        headlines=Selector(response).xpath('//h3[@class="lx-stream-post__header-title gel-great-primer-bold qa-post-title gs-u-mt0 gs-u-mb-"]')
        item=NewsItem()
        for headline in headlines:
            item['title']=headline.xpath('a/span/text()').extract()[0]
            item['url']='https://www.bbc.com'+headline.xpath('a/@href').extract()[0]
            yield item