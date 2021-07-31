import unittest
from tests.test_wealth_manager import TestCalculate, TestGetNetWorth, \
    TestGetApartmentsNeeded


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculate('test_calculate_easy_first'))
    suite.addTest(TestCalculate('test_calculate_medium_second'))
    suite.addTest(TestCalculate('test_calculate_hard_first'))

    suite.addTest(TestGetNetWorth('test_net_worth_easy_first'))
    suite.addTest(TestGetNetWorth('test_net_worth_easy_second'))

    suite.addTest((TestGetApartmentsNeeded(
        'test_apartments_needed_easy_first')))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
