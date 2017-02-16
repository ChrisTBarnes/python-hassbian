from setuptools import setup

from hassbian import __version__

setup(
    name='Hassbian',
    packages=['hassbian'],
    version=__version__,
    description='A python library to help administrative tasks on Hassbian.',
    author='Paulus Schoutsen',
    author_email='paulus@paulusschoutsen.nl',
    url='https://github.com/home-assistant/python-hassbian/',
    download_url=('https://github.com/home-assistant/python-hassbian/'
                  'tarball/{}'.format(__version__)),
)
