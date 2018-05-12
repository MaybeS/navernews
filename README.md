# navernews
[![Pypi](https://img.shields.io/pypi/v/navernews.svg)](https://pypi.python.org/pypi/navernews)
[![Python Versions](https://img.shields.io/pypi/pyversions/navernews.svg)](https://pypi.python.org/pypi/navernews)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Naver News crawling utility

## Usage

```
from navernews import News as NN

for news in NN.crawl('keyword'):
    print (news.text)
```
