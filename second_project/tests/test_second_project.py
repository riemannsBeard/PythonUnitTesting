import unittest
from second_project import Counter


class EasyTestCase(unittest.TestCase):
    # Order of execution:
    # 1. setUp method
    # 2. One of the methods to be tested (in order of definition)
    # 3. tearDown method
    # 4. Go to 1.

    # It is needed whenever an object is instantiated to be tested.
    # It has to be executed first.
    def setUp(self):
        self.counter = Counter()

    def test_easy_input(self):
        self.assertEqual(self.counter.get_value(), 0)

    def test_easy_input_two(self):
        self.counter.clear()
        self.assertEqual(self.counter.get_value(), 0)

    # It is complementary to setUp and is needed to put the object down after
    # the test.
    # It has to be executed at the end of the class
    def tearDown(self):
        # pass
        self.counter = None