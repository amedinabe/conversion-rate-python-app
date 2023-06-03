import unittest
from currency import CurrencyConverter

class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the CurrencyConverter class from currency.py
    """
    def setUp(self):
        self.date = '2021-01-01'
        self.from_currency = 'GBP'
        self.to_currency = 'AUD'
    
    def test_converter_instantiation(self):
        currency = CurrencyConverter(from_currency = self.from_currency, to_currency = self.to_currency, date = self.date)
    
        self.assertEqual(currency.date, self.date)
        self.assertEqual(currency.from_currency, self.from_currency)
        self.assertEqual(currency.to_currency, self.to_currency)


class TestCurrencyCheck(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """
    def setUp(self):
        self.date = '2021-01-01'
        self.test_currency_1 = 'GBP'
        self.test_currency_2 = 'AUD'
        self.test_currency_3 = 'aaa'
        self.test_currency_4 = 'BBB'
        self.test_currency_5 = 'USD'
        self.test_currency_6 = 'EURR'
        self.test_currency_7 = 'AU'
        self.test_currency_8 = None
        self.test_currency_9 = 'GBP*'
        self.test_currency_10 = ''
        self.test_currency_11 = 123
        self.test_currency_12 = '123'
    
    def test_check_currencies(self):
        currency1 = CurrencyConverter(from_currency = self.test_currency_1, to_currency = self.test_currency_2, date = self.date)
        currency2 = CurrencyConverter(from_currency = self.test_currency_1, to_currency = self.test_currency_3, date = self.date)
        currency3 = CurrencyConverter(from_currency = self.test_currency_2, to_currency = self.test_currency_4, date = self.date)
        currency4 = CurrencyConverter(from_currency = self.test_currency_5, to_currency = self.test_currency_6, date = self.date)
        currency5 = CurrencyConverter(from_currency = self.test_currency_1, to_currency = self.test_currency_7, date = self.date)
        currency6 = CurrencyConverter(from_currency = self.test_currency_1, to_currency = self.test_currency_8, date = self.date)
        currency7 = CurrencyConverter(from_currency = self.test_currency_1, to_currency = self.test_currency_9, date = self.date)
        currency8 = CurrencyConverter(from_currency = self.test_currency_10, to_currency = self.test_currency_2, date = self.date)
        currency9 = CurrencyConverter(from_currency = self.test_currency_11, to_currency = self.test_currency_2, date = self.date)
        currency10 = CurrencyConverter(from_currency = self.test_currency_12, to_currency = self.test_currency_2, date = self.date)
        
        self.assertEqual(currency1.check_currencies(), True)
        self.assertEqual(currency2.check_currencies(), False)
        self.assertEqual(currency3.check_currencies(), False)
        self.assertEqual(currency4.check_currencies(), False)
        self.assertEqual(currency5.check_currencies(), False)
        self.assertEqual(currency6.check_currencies(), False)
        self.assertEqual(currency7.check_currencies(), False)
        self.assertEqual(currency8.check_currencies(), False)
        self.assertEqual(currency9.check_currencies(), False)
        self.assertEqual(currency10.check_currencies(), False)
            
        
        
class TestReverseRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """
    def setUp(self):
        self.date = '2021-01-01'
        self.test_currency_1 = 'GBP'
        self.test_currency_2 = 'AUD'
        
    def test_reverse_rate(self):
        currency1 = CurrencyConverter(from_currency = self.test_currency_1, to_currency = self.test_currency_2, date = self.date)
        currency1.rate = 1.8649
        currency1.reverse_rate()
        
        currency2 = CurrencyConverter(from_currency = self.test_currency_1, to_currency = self.test_currency_2, date = self.date)
        currency2.rate = 1
        currency2.reverse_rate()
        
        currency3 = CurrencyConverter(from_currency = self.test_currency_1, to_currency = self.test_currency_2, date = self.date)
        currency3.rate = 0
        currency3.reverse_rate()
    
        
        self.assertEqual(0.5362 , currency1.inverse_rate)
        self.assertEqual(1 , currency2.inverse_rate)
        self.assertEqual(0 , currency3.inverse_rate)                            
    
class TestRoundRate(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """
    def setUp(self):
        self.date = '2021-01-01'
        self.test_currency_1 = 'GBP'
        self.test_currency_2 = 'AUD'
        
    def test_round_rate(self):
        currency1 = CurrencyConverter(from_currency = self.test_currency_1, to_currency = self.test_currency_2, date = self.date)
        currency1.rate = 1.864911
        round_rate1 = currency1.round_rate(rate = currency1.rate)
        
        currency2 = CurrencyConverter(from_currency = self.test_currency_1, to_currency = self.test_currency_2, date = self.date)
        currency2.rate = 0
        round_rate2 = currency1.round_rate(rate = currency1.rate)
        
        self.assertEqual(1.8649 , round_rate1)
        self.assertEqual(1.8649 , round_rate2)
        

class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """
    def setUp(self):
        self.date = '2021-01-01'
        self.from_currency = 'GBP'
        self.to_currency = 'AUD'
    
    def test_get_historical_rate(self):
        currency = CurrencyConverter(from_currency = self.from_currency, to_currency = self.to_currency, date = self.date)
        currency.get_historical_rate()
        
        self.assertIsNotNone(currency.rate)
        self.assertIsNotNone(currency.inverse_rate)
        self.assertIsNotNone(currency.frankfurter)
        
if __name__ == '__main__':
    unittest.main()