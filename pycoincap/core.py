import requests


class Coin(object):
    def __init__(self, coin_info):
        self.id = id
        self.coin_info = coin_info

    def __str__(self):
        info = "Coin: %s \nRanked: %s" % (self.coin_info['name'],
                                          self.coin_info['rank'])
        info += "\nPrice : %s $ \nPrice BTC: %s " % (
            self.coin_info['price_usd'], self.coin_info['price_btc'])
        info += "\nCirculating supply: %s \nTotal supply: %s"\
                %(self.coin_info['available_supply'],
                  self.coin_info['total_supply'])
        info += "\nPercent changes:1h  = %s\n \t\t24h = %s\n \t\t7d  = %s" \
                %(self.coin_info['percent_change_1h'],
                  self.coin_info['percent_change_24h'],
                  self.coin_info['percent_change_7d'])
        return info

    def __repr__(self):
        return "Coin"


class Stats(object):

    def __init__(self,
                 btc_market_percent="",
                 total_market_usd="",
                 active_market="",
                 active_assets="",
                 active_currencies="",
                 last_day_volume_usd=""):
        self.btc_market_percent = btc_market_percent
        self.total_market_usd = total_market_usd
        self.active_market = active_market
        self.active_assets = active_assets
        self.active_currencies = active_currencies
        self.last_day_volume_usd = last_day_volume_usd

    def __str__(self):
        statistics = " Market value: %s$" % self.total_market_usd
        statistics += "\n Bitcoin percentage: %s" % self.btc_market_percent
        statistics += "\n Active markets: %s" % self.active_market
        statistics += "\n Active assets: %s" % self.active_assets
        statistics += "\n Active currencies: %s" % self.active_currencies
        statistics += "\n Last day changes: %s" % self.last_day_volume_usd
        return statistics

    def __repr__(self):
        return "Stats"


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

    def coin(self,  coin_id, **kwargs):
        '''

        :param coin_id: Name of coin e.g bitcoin
        :param kwargs: Optional parameters:
                (int) start - return results from rank [start] and above
                (int) limit - return a maximum of [limit] results
                (string) convert - return price, 24h volume, and market cap in
                terms of another currency. Valid values are:
                "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR",
                "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN",
                "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD",
                "THB", "TRY", "TWD", "ZAR"

        :return:  Returns a object containing the info for currencie
        '''
        params = {}
        params.update(**kwargs)
        data = self.__call_market('ticker/{coin_id}'.format(coin_id=coin_id), params)
        coin = data[0]
        return Coin(coin['id'], coin)

    def stats(self, **kwargs):
        '''

        :param kwargs: Optional parameters:
        (string) convert - return 24h volume, and market cap
        in terms of another currency. Valid values are:
         "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR",
                "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN",
                "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD",
                "THB", "TRY", "TWD", "ZAR"
        :return: Returns object that contains cryptocurrency statistics.
        '''
        params = {}
        params.update(**kwargs)
        data = self.__call_market('global', params)
        return Stats(data['bitcoin_percentage_of_market_cap'],
                     data['total_market_cap_usd'],
                     data['active_markets'], data['active_assets'],
                     data['active_currencies'], data['total_24h_volume_usd'])
