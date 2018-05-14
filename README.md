# navertools

Naver tools for python

## Usage

```
import navertools

for news in navertools.news('2018-05-14', '2018-05-20'):
    for comment in news.comments():
        print (comment.text)
```
