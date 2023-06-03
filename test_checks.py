import unittest
from checks import check_arguments, check_date


class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """
        
    def test_check_arguments(self):
        
        date = '2021-01-01'
        from_currency = 'GBP'
        to_currency = 'AUD'
        
        args_test1 = []
        args_test2 = [from_currency, to_currency]
        args_test3 = [date, from_currency]
        args_test4 = [date]
        args_test5 = [date, from_currency, to_currency, to_currency]
        args_test6 = [date, from_currency, to_currency]
        
        self.assertEqual(check_arguments(args_test1), False)
        self.assertEqual(check_arguments(args_test2), False)
        self.assertEqual(check_arguments(args_test3), False)
        self.assertEqual(check_arguments(args_test4), False)
        self.assertEqual(check_arguments(args_test5), False)
        self.assertEqual(check_arguments(args_test6), True)
        return
             

class TestCheckDate(unittest.TestCase):
    """
    Class used for testing the check_date() function from checks.py
    """
        
    def test_check_date(self):
        args_test1 = '20210101'
        args_test2 = '2021/01/01'
        args_test3 = '01-01-2021'
        args_test4 = '01/01/2021'
        args_test5 = '2021.01.01'
        args_test6 = '01.01.2021'
        args_test7 = '2021/01/01'
        args_test8 = '*2021*01*01'
        args_test9 = '2021-01'
        args_test10 = '*2021-01-01'
        args_test11 = '20210-01-01'
        args_test12 = '02021-01-01'
        args_test13 = '2021-001-01'
        args_test14 = '2021-01-001'
        args_test15 = '2021-11-16'
        args_test16 = '2021-01-01'
        
        
        self.assertEqual(check_date(args_test1), False)
        self.assertEqual(check_date(args_test2), False)
        self.assertEqual(check_date(args_test3), False)
        self.assertEqual(check_date(args_test4), False)
        self.assertEqual(check_date(args_test5), False)
        self.assertEqual(check_date(args_test6), False)
        self.assertEqual(check_date(args_test7), False)
        self.assertEqual(check_date(args_test8), False)
        self.assertEqual(check_date(args_test9), False)
        self.assertEqual(check_date(args_test10), False)
        self.assertEqual(check_date(args_test11), False)
        self.assertEqual(check_date(args_test12), False)
        self.assertEqual(check_date(args_test13), False)
        self.assertEqual(check_date(args_test14), False)
        self.assertEqual(check_date(args_test15), True)
        self.assertEqual(check_date(args_test16), True)
        
        return

if __name__ == '__main__':
    unittest.main()