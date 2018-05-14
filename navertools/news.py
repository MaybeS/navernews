from typing import Generator, Tuple, List

from .lib.connections import request
from .lib.utility import get_context

class News:
    def __init__(self, config=None):
        pass

    @staticmethod
    def get_press(label: bool = True) -> Generator[str, None, None]:
        """ get press list
        """
        ext = lambda e: e.text if label else e.get('class').split(',')[1][:-1]
        url = 'http://news.naver.com/main/ajax/bottomIndex/press.nhn'
        for press in get_context(request(url)).xpath('//ul/li/a'):
            if ',' in press.get('class'):
                yield ext(press)

    @staticmethod
    def get_category(label: bool = True) -> Generator[Tuple[str, List[str]], None, None]:
        """ get category list
        """
        ext = lambda e: e.text if label else e.get('class').split(',')[1][:-1]
        url = 'http://news.naver.com/main/ajax/bottomIndex/category.nhn'
        for div in get_context(request(url)).xpath('//div'):
            if not div.xpath('./h5/a'): continue
            yield ext(div.xpath('./h5/a')[0]), [
                ext(sub) for sub in div.xpath('./ul/li/a') if ',' in sub.get('class')
            ]
