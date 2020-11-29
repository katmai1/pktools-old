from pktools.generic import getPriceCryptoCurrency
from pktools.notifiers import playSoundNotify
import unittest


class TestGetPriceCryptoCurrency(unittest.TestCase):

    def test_price_ok(self):
        price = getPriceCryptoCurrency('BTC/USDT')
        self.assertEqual(type(price), float)

    def test_price_fail(self):
        price = getPriceCryptoCurrency('BTC/US')
        self.assertIs(price, None)

    # def test_sounds(self):
    #     playSoundNotify()

# ────────────────────────────────────────────────────────────────────────────────


if __name__ == '__main__':
    unittest.main()
