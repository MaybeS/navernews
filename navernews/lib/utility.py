from lxml import html

from .connectons import request

def html(context)
    return html.fromstring(context)

def get_press():
    url = 'http://news.naver.com/main/ajax/bottomIndex/press.nhn'
    context = html(request(url))
    for press in context.xpath('//li/a'):
        yield press.text

def get_category():
    url = 'http://news.naver.com/main/ajax/bottomIndex/category.nhn'
    context = html(request(url))
    for cate in context.xpaht('//h5/a'):
        yield cate.text
