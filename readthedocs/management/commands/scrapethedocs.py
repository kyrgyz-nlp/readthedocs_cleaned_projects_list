from django.core.management.base import BaseCommand, CommandError
from scrapy.crawler import CrawlerProcess

from readthedocs.models import Project
from readthedocs.scraper.spiders.readthedocs_generic import ReadthedocsSpider


class Command(BaseCommand):
    help = 'Scrapes projects documentations'

    def handle(self, *args, **kwargs):
        url = 'https://webgrep.readthedocs.io/en/latest/'
        allowed_domains = ['readthedocs.io', 'github.com']
        projects = Project.objects.filter(documentation_type='mkdocs')
        process = CrawlerProcess()
        process.crawl(
            ReadthedocsSpider,
            allowed_domains=allowed_domains,
            projects=projects)
        process.start()
