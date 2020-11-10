from pktools.generic import getPriceCryptoCurrency
import unittest


class TestGetPriceCryptoCurrency(unittest.TestCase):

    def test_price_ok(self):
        price = getPriceCryptoCurrency('BTC/USDT')
        self.assertEqual(type(price), float)

    def test_price_fail(self):
        price = getPriceCryptoCurrency('BTC/US')
        self.assertIs(price, None)

# ────────────────────────────────────────────────────────────────────────────────


if __name__ == '__main__':
    unittest.main()
