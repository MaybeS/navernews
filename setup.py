from setuptools import setup, find_packages
from pythond import __version__
setup(
    name             = 'navertools',
    version          = __version__,
    description      = 'Naver tools for python',
    author           = 'Maydev',
    author_email     = 'alice.maydev@gmail.com',
    url              = 'https://github.com/MaybeS/navertools',
    download_url     = 'https://githur.com/MaybeS/navertools/archive/1.0.tar.gz',
    install_requires = [ ],
    license          = 'LGPL',
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['naver', 'tools', 'news'],
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