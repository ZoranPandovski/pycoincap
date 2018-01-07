
<h1 align="center">
	<img width="400" src="https://cdn-images-1.medium.com/max/1024/1*TY0eUcLT6us5Jz1VT1Tymg.jpeg" alt="Cryptocurrencies">
	<br>
	<br>
</h1>


![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/ZoranPandovski/pycoincap.svg?branch=master)](https://github.com/ZoranPandovski/pycoincap)
[![Coverage Status](https://coveralls.io/repos/github/ZoranPandovski/pycoincap/badge.svg?branch=master)](https://coveralls.io/github/ZoranPandovski/pycoincap?branch=master)

# Pycoincap
Python module for getting cryptocurrency data from Coinmarketcap

# Run tests
```
 python -m unittests pycoincap.tests.test_core
```

## Installation:

From source use
```
   git clone https://github.com/ZoranPandovski/pycoincap
   cd pycoincap
   python setup.py
   pip install -r requirements.txt
```

## Examples:
Retrieve informations from https://coinmarketcap.com/

Get coin informations
```python
from pycoincap import CryptoMarket as market

# Load data data from coinmarketcap
m = market()

# Returns coin object
BTC = m.coin('bitcoin')

print BTC
>>> Coin: Bitcoin
    Ranked: 1
    Price : 4775.44 $
    Price BTC: 1.0
    Available supply: 16613825.0
    Total supply: 16613825.0
    Percent changes:1h  = -0.89
            24h = 8.35
            1d  = 3.74

print BTC.price_usd
>>> 4775.44
```

Get stats
```python
from pycoincap import CryptoMarket as market

# Load data data from coinmarketcap
m = market()

#Returns stats
stats = m.stats()

print stats
>>>  Market value: 52.41$
     Bitcoin percentage: 1.51106247425e+11
     Active markets: 5665
     Active assets: 279
     Active currencies: 874
     Last day changes: 4451850464.0
```
