import io
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='PixivWebPy',
    packages=['pixivwebpy'],
    version= '0.0.1',
    description='A Pixiv Web API',
    long_description=io.open('README.md', mode='r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author='Rorical',
    author_email='rorical@shugetsu.space',
    install_requires=["requests>=2.22.0"],
    url='https://github.com/Rorical/pixiv-web-py',
    download_url='https://github.com/Rorical/pixiv-web-py/releases',
    keywords=['pixiv', 'api', 'pixiv web api'],
        classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)