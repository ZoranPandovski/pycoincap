import requests


class Coin(object):
    def __init__(self,
                 id="",
                 name="",
                 symbol="",
                 rank="",
                 price_usd="",
                 price_btc="",
                 market_cap_usd="",
                 available_supply="",
                 total_supply="",
                 percent_change_1h="",
                 percent_change_24h="",
                 percent_change_7d="",
                 last_updated="",
                 last_day_volume_usd=""):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.rank = rank
        self.price_usd = price_usd
        self.price_btc = price_btc
        self.market_cap_usd = market_cap_usd
        self.available_supply = available_supply
        self.total_supply = total_supply
        self.percent_change_1h = percent_change_1h
        self.percent_change_24h = percent_change_24h
        self.percent_change_7d = percent_change_7d
        self.last_updated = last_updated
        self.last_day_volume_usd = last_day_volume_usd

    def __str__(self):
        info = "Coin: %s \nRanked: %s" % (self.name, self.rank)
        info += "\nPrice : %s $ \nPrice BTC: %s " % (self.price_usd,
                                                   self.price_btc)
        info += "\nAvailable supply: %s \nTotal supply: %s"\
                %(self.available_supply, self.total_supply)
        info += "\nPercent changes:1h  = %s\n \t\t24h = %s\n \t\t1d  = %s" \
                %(self.percent_change_1h, self.percent_change_7d,
                  self.percent_change_24h)
        return info

    def __repr__(self):
        return "Coin"


class CryptoMarket(object):
    __COIN_MARKET_CAP_URL = \
        'https://api.coinmarketcap.com/v1/'

    def __call_market(self, endpoint, params):
        try:
            response = requests.get(
                self.__COIN_MARKET_CAP_URL + endpoint, params=params)
            if response.status_code != '200':
                response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise e
        data = response.json()
        return data

    def get_coin(self, name, **kwargs):
        params = {}
        params.update(**kwargs)
        data = self.__call_market(name, params)
        if 'error' in data:
            return 'Error occurred'
        coin = data[0]
        return Coin(coin['id'], coin['name'], coin['symbol'], coin['rank'],
                    coin['price_usd'], coin['price_btc'],
                    coin['market_cap_usd'], coin['available_supply'],
                    coin['total_supply'], coin['percent_change_1h'],
                    coin['percent_change_24h'], coin['percent_change_7d'],
                    coin['last_updated'], coin['24h_volume_usd'])

    def get_stats(self, **kwargs):
        params = {}
        params.update(**kwargs)
        data = self.__call_market('global', params)
        return data
