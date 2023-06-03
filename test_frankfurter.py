import unittest
from frankfurter import Frankfurter
import validators

class TestUrl(unittest.TestCase):
    """
    Class used for testing the url attributes of the Frankfurter class from frankfurter.py
    """

    def test_url(self):
        frankfurter = Frankfurter()
        
        self.assertEqual(validators.url(frankfurter.base_url), True)
        self.assertEqual(validators.url(frankfurter.currencies_url), True)
        self.assertEqual(validators.url(frankfurter.historical_url), True)

class TestCurrenciesList(unittest.TestCase):
    """
    Class used for testing the currencies attribute of the Frankfurter class from frankfurter.py
    """

    def test_get_currencies_list(self):
        frankfurter = Frankfurter()
        python_list = frankfurter.get_currencies_list()
        
        self.assertIsNotNone(python_list)
        self.assertNotEqual(len(python_list), 0)
        #self.assertEqual(type(python_list), "<class 'list'>")
        
class TestCheckCurrency(unittest.TestCase):
    """
    Class used for testing the Frankfurter.check_currency() method from frankfurter.py
    """

    def test_check_currency(self):
        frankfurter = Frankfurter()
        is_currency_valid1 = frankfurter.check_currency('AUD')
        is_currency_valid2 = frankfurter.check_currency('AAA')
        is_currency_valid3 = frankfurter.check_currency('')
        is_currency_valid4 = frankfurter.check_currency('bbb')
        is_currency_valid5 = frankfurter.check_currency(None)
        is_currency_valid6 = frankfurter.check_currency(123)
        is_currency_valid7 = frankfurter.check_currency('AUDD')
        is_currency_valid8 = frankfurter.check_currency('AU')
        
        self.assertEqual(is_currency_valid1, True)
        self.assertEqual(is_currency_valid2, False)
        self.assertEqual(is_currency_valid3, False)
        self.assertEqual(is_currency_valid4, False)
        self.assertEqual(is_currency_valid5, False)
        self.assertEqual(is_currency_valid6, False)
        self.assertEqual(is_currency_valid7, False)
        self.assertEqual(is_currency_valid8, False)


class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the Frankfurter.get_historical_rate() method from frankfurter.py
    """

    def setUp(self):
        self.from_date = '2021-01-01'
        self.from_currency = 'GBP'
        self.to_currency = 'AUD'
        
    def test_get_historical_rate(self):
        frankfurter = Frankfurter()
        response = frankfurter.get_historical_rate(self.from_currency, self.to_currency, self.from_date)
        
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.json())
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()