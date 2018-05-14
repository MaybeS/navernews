from lxml import html

def get_context(text) -> html.HtmlElement:
    """ get html document context
    """
    return html.fromstring(text)
