import requests
from polyglot.detect import Detector
from polyglot.detect.base import UnknownLanguage
from django.core.management.base import BaseCommand, CommandError
from readthedocs.models import Project


def _get_data(url):
    r = requests.get(url)
    return r.json()


def _detect_lang(text):
    try:
        for lang in Detector(text).languages:
            print('=======', lang.confidence > 80, '=======')
            if lang.confidence > 80:
                return lang.code
    except:
        return 'unknown'
    return 'mixed'


def _get_and_write(url):
    #initial = _get_data('https://readthedocs.org/api/v2/project/')
    data = _get_data(url)
    results = data.get('results', [])
    objects = [
        Project(
            project_id=r['id'],
            name=r['name'],
            slug=r['slug'],
            programming_language=r['programming_language'],
            default_version=r['default_version'],
            repo_type=r['repo_type'],
            repo=r['repo'],
            description=r['description'],
            language=r['language'],
            documentation_type=r['documentation_type'],
            canonical_url=r['canonical_url'],
            actual_language=_detect_lang(r['description'])) for r in results]
    Project.objects.bulk_create(objects)
    next_url = data.get('next')
    if next_url:
        print('@@@@@', next_url, '@@@@@')
        _get_and_write(next_url)


class Command(BaseCommand):
    help = 'Requests data from ReadTheDocs APIv2 and writes to DB'

    def handle(self, *args, **kwargs):
        url = 'https://readthedocs.org/api/v2/project/'
        _get_and_write(url)
