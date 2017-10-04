from distutils.core import setup

setup(
   name='pycoincap',
   version='1.0.0',
   url = 'https://github.com/ZoranPandovski/pycoincap',
   description='Module for getting cryptocurrency data from Coinmarketcap',
   author='Zoran Pandovski',
   author_email='zoran.pandovski@gmail.com',
   packages=['pycoincap'],
   install_requires=['requests']
)