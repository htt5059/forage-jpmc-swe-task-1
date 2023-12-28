import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price = (bid_price+ask_price)/2
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price = (bid_price+ask_price)/2
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], price))


  def test_getRatio_calculateRatio(self):
    prices = [
      {'a': 5, 'b': 10},
      {'a': 3, 'b': 1}
    ]

    for price in prices:
      ratio = price['a']/price['b']
      self.assertEqual(getRatio(price['a'], price['b']), ratio)

  def test_getRatio_calculateRatioPriceBIsZero(self):
    prices = [
      {'a': 5, 'b': 0},
      {'a': 3, 'b': 0}
    ]

    for price in prices:
      self.assertEqual(getRatio(price['a'], price['b']), None)

  


if __name__ == '__main__':
    unittest.main()
