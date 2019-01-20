import scrapy
import scrapy.exceptions import CloseSpider


class ReadthedocsSpider(scrapy.Spider):
    name = 'readthedocs'

    def __init__(self, allowed_domains=[], projects=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [p.canonical_url for p in projects]
        self.allowed_domains = allowed_domains
        self.projects = projects

    def parse(self, response):
        print('PPAAARRRSSSIINNGGG')
        url = response.url
        if not self.projects:
            raise CloseSpider('projects queryset should be passed')
        project = self.projects.filter(canonical_url=url).first()
        try:
            print('SLUG HERE', project.slug)
            i = {}
            i['url'] = url
            i['slug'] = slug
            return i
        except:
            print('something went wrong')
            return {}
