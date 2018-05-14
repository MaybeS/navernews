from urllib.parse import unquote

from lxml import html

def get_context(text: str) -> html.HtmlElement:
    """ get html document context
    """
    return html.fromstring(text)

def decode_url(url: str) -> str:
    return unquote(url)

def encode_url(url: str) -> str:
    return quote(url)
