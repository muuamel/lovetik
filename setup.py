from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'With This Package Can You Download Any TikTok Video from lovetik.com'
LONG_DESCRIPTION = 'With This Package Can You Download Any TikTok Video from lovetik.com'

# Setting up
setup(
    name="lovetik",
    version=VERSION,
    author="Muamel Ameer",
    author_email="amowallet@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['tiktok'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    url='https://github.com/muamelAmeer/tiktokdow',
    project_urls={
        'Source': 'https://github.com/muamelAmeer/tiktokdow',
        'Dev Lib': 'https://github.com/muamelAmeer',
        'Documentation': 'https://github.com/muamelAmeer/tiktokdow'
    },
)
