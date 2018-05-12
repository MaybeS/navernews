from setuptools import setup, find_packages
from pythond import __version__
setup(
    name             = 'navernews',
    version          = __version__,
    description      = 'Naver News crawling utility',
    author           = 'Maydev',
    author_email     = 'alice.maydev@gmail.com',
    url              = 'https://github.com/MaybeS/navernews',
    download_url     = 'https://githur.com/MaybeS/navernews/archive/1.0.tar.gz',
    install_requires = [ ],
    license          = 'LGPL',
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['naver', 'news', 'crawler'],
    package_data     = {},
    zip_safe         = False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)