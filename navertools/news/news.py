from typing import Generator, Tuple, List
from itertools import chain

from .config import CONFIG
from ..lib.connections import request
from ..lib.utility import get_context, assert_date, flatten

class News:
    """ Naver News class
    """

    __press_url = 'http://news.naver.com/main/ajax/bottomIndex/press.nhn'
    __cate_url = 'http://news.naver.com/main/ajax/bottomIndex/category.nhn'
    __url = 'http://news.naver.com/main/list.nhn?sid1={cate1}&sid2={cate2}&page={page}&oid={press}&date={date}'

    __press = None
    __cate = None

    def __init__(self, config=None):
        self.config = CONFIG.copy()
        if config: self.config.update(config)

    def __iter__(self):
        return self

    def __next__(self):
        if self.assert_iter(): raise StopIteration
        try:
            return self.current
        finally:
            self.current += 1

    @property
    def date(self):
        return self.config['date_from'], self.config['date_to']

    @date.setter
    def date(self, date):
        assert all(map(assert_date, date)), 'Date format must be 0000-00-00'
        self.config['date_from'], self.config['date_to'] = date

    @property
    def _press(self):
        News.__press = News.__press or list(News.get_press())
        return News.__press

    @property
    def press(self):
        return self.config['press']

    @press.setter
    def press(self, press):
        assert press in self._press or not press, 'Invalid press'
        self.config['press'] = press

    @property
    def _category(self):
        News.__cate = News.__cate or list(News.get_category())
        return News.__cate

    @property
    def category(self):
        return self.config['cate']

    @category.setter
    def category(self, cate):
        assert cate in flatten(self._category) or not cate, 'Invalide category'
        self.config['cate'] = cate

    def wrapper(self) -> str:
        return News.__url.format(**self.config)

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
