from typing import Generator, Tuple, List

from .config import CONFIG
from ..lib.connections import request
from ..lib.utility import get_context

class News:
    """ Naver News class
    """
    __press_url = 'http://news.naver.com/main/ajax/bottomIndex/press.nhn'
    __cate_url = 'http://news.naver.com/main/ajax/bottomIndex/category.nhn'
    __url = 'https://search.naver.com/search.naver?where=news&query={keyword}&nso={date}&field={target}'

    def __init__(self, config=None):
        self.config = CONFIG.copy()
        if config: self.config.update(config)

        assert self.config['keyword'], 'Set keyword!'

    @property
    def keyword(self):
        return self.config['keyword']

    @property
    def date_from(self):
        return self.config['date_from']

    @property
    def date_to(self):
        return self.config['date_to']

    @property
    def target(self):
        return self.config['target']

    @target.setter
    def target(self, tar):
        assert tar in ['all', 'title'], 'Must be all or title'
        self.config['target'] = tar == 'title'

    def wrapper(self) -> str:
        return __url.format(**self.config)

    @staticmethod
    def get_press(label: bool = True) -> Generator[str, None, None]:
        """ get press list
        """
        ext = lambda e: e.text if label else e.get('class').split(',')[1][:-1]
        for press in get_context(request(News.__press_url)).xpath('//ul/li/a'):
            if ',' in press.get('class'):
                yield ext(press)

    @staticmethod
    def get_category(label: bool = True) -> Generator[Tuple[str, List[str]], None, None]:
        """ get category list
        """
        ext = lambda e: e.text if label else e.get('class').split(',')[1][:-1]
        for div in get_context(request(News.__cate_url)).xpath('//div'):
            if not div.xpath('./h5/a'): continue
            yield ext(div.xpath('./h5/a')[0]), [
                ext(sub) for sub in div.xpath('./ul/li/a') if ',' in sub.get('class')
            ]
