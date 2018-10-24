import unittest
import requests
import pytest
from mock import patch, Mock
from pycoincap import CryptoMarket as market


class TestCore(unittest.TestCase):

    def assertCoin(self, coin, coin_id, coin_name, coin_symbol):
        self.assertEqual(coin.id, coin_id)
        self.assertEqual(coin.name, coin_name)
        self.assertEqual(coin.symbol, coin_symbol)
        self.assertTrue(int(coin.rank))
        self.assertTrue(float(coin.price_usd))
        self.assertTrue(float(coin.price_btc))
        self.assertTrue(float(coin.market_cap_usd))
        self.assertTrue(float(coin.available_supply))
        self.assertTrue(float(coin.total_supply))
        self.assertTrue(float(coin.percent_change_1h))
        self.assertTrue(float(coin.percent_change_24h))
        self.assertTrue(float(coin.percent_change_7d))
        self.assertTrue(float(coin.last_updated))
        self.assertTrue(float(coin.last_day_volume_usd))
        self.assertTrue(str(coin.__str__()))
        self.assertTrue("Coin",coin.__repr__())

    def assertStats(self, stats):
        self.assertTrue(float(stats.btc_market_percent))
        self.assertTrue(float(stats.total_market_usd))
        self.assertTrue(int(stats.active_market))
        self.assertTrue(int(stats.active_assets))
        self.assertTrue(int(stats.active_currencies))
        self.assertTrue(float(stats.last_day_volume_usd))
        self.assertTrue(str(stats.__str__()))
        self.assertTrue("Stats",stats.__repr__())

    def test_bitcoin(self):
        m = market()
        coin = m.coin('bitcoin')
        self.assertCoin(coin,'bitcoin', 'Bitcoin', 'BTC')

    def test_ethereum(self):
        m = market()
        coin = m.coin('ethereum')
        self.assertCoin(coin,'ethereum', 'Ethereum', 'ETH')

    def test_stats(self):
        m = market()
        stats = m.stats()
        self.assertStats(stats)

    @patch('pycoincap.core.requests.get')
    def test_HttpError(self, get_mock):
        http_error = requests.exceptions.HTTPError('Unable to connect')
        mock_raise_for_status = Mock(side_effect=http_error)
        get_mock.raise_for_status = mock_raise_for_status
        get_mock.side_effect = http_error

        m = market()

        with pytest.raises(requests.exceptions.HTTPError):
            m.coin('bitcoin')

    def test_coin_str(self):
        m = market()
        coin = m.coin('bitcoin')
        self.assertIn("Coin:", str(coin))

    def test_coin_repr(self):
        m = market()
        coin = m.coin('bitcoin')
        self.assertEqual("Coin", repr(coin))

    def test_stats_str(self):
        m = market()
        stats = m.stats()
        self.assertIn("Market value:", str(stats))

    def test_stats_repr(self):
        m = market()
        stats = m.stats()
        self.assertEqual("Stats", repr(stats))


if __name__ == '__main__':
    unittest.main()
