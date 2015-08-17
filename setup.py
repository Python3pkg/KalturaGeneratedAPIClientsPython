from distutils.core import setup
from setuptools import find_packages

setup(
    name='KalturaClient',
    version='1.0.0',
    url='http://www.kaltura.com/api_v3/testme/client-libs.php',
    packages=['KalturaClient', 'KalturaClient.Plugins'],
    #packages=find_packages(),
    license='AGPL',
    description='A Python module for accessing the Kaltura API.',
    long_description=open('README.txt').read(),
    install_requires = [
            'poster',
        ],
    author='Patrick Tchankue',
    keywords = ['kaltura', 'python'], # arbitrary keywords
    url = 'https://github.com/ptchankue/KalturaGeneratedAPIClientsPython',
    download_url = 'https://github.com/ptchankue/KalturaGeneratedAPIClientsPython/tarball/0.1',
)
