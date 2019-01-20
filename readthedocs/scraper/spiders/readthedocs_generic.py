import scrapy

class ReadthedocsSpider(scrapy.Spider):
    name = 'readthedocs'

    def __init__(self, allowed_domains=[], start_urls=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = start_urls
        self.allowed_domains = allowed_domains
        
        print('@@@@', allowed_domains)
        print('####', start_urls)

    def parse(self, response):
        print('PPAAARRRSSSIINNGGG')
        i = {}
        i['url'] = response.url
        return i
