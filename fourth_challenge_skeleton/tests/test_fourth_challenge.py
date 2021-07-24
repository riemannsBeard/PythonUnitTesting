import time
import unittest
from fourth_challenge import EfficiencyAdding


class TestEfficiency(unittest.TestCase):

    def setUp(self):
        # Default constructor
        self._efficiency = EfficiencyAdding()
        self._efficiency_data = dict()

    def test_first_adding_method(self):
        # Todo: start timing your program.
        self._start_time = time.time()
        # Todo: use the object self._efficiency to call the
        #  adding_two_first_method.
        self._efficiency.adding_two_first_method(100)
        #  Todo: end timing your program.
        self._end_time = time.time()
        #  Todo: add the result to self._efficiency_data dictionary.
        self._efficiency_data['first method'] = self._end_time - \
                                                self._start_time

    def test_second_adding_method(self):
        # Todo: start timing your program.
        self._start_time = time.time()
        # Todo: use the object self._efficiency to call the
        #  adding_two_second_method.
        self._efficiency.adding_two_second_method(100)
        #  Todo: end timing your program.
        self._end_time = time.time()
        #  Todo: add the result to self._efficiency_data dictionary.
        self._efficiency_data['second method'] = self._end_time - \
                                                 self._start_time

    def tearDown(self):
        print(self._efficiency_data)
        self._efficiency = None


if __name__ == '__main__':
    unittest.main()
