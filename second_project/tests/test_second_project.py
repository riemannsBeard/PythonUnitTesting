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


class MediumTestCase(unittest.TestCase):
    # Order of execution:
    # 1. setUp method
    # 2. One of the methods to be tested (in order of definition)
    # 3. tearDown method
    # 4. Go to 1.

    # It is needed whenever an object is instantiated to be tested.
    # It has to be executed first.
    def setUp(self):
        self.counter = Counter()

    def test_medium_input(self):
        self.counter.add()
        self.counter.add()
        self.counter.add()
        self.assertEqual(self.counter.get_value(), 3)

    def test_medium_input_two(self):
        self.counter.add()
        self.counter.add()
        self.counter.add()
        self.counter.remove()
        self.counter.remove()
        self.assertEqual(self.counter.get_value(), 1)

    # It is complementary to setUp and is needed to put the object down after
    # the test.
    # It has to be executed at the end of the class
    def tearDown(self):
        # pass
        self.counter = None


class HardTestCase(unittest.TestCase):
    # Order of execution:
    # 1. setUp method
    # 2. One of the methods to be tested (in order of definition)
    # 3. tearDown method
    # 4. Go to 1.

    # It is needed whenever an object is instantiated to be tested.
    # It has to be executed first.
    def setUp(self):
        self.counter = Counter()

    def test_hard_input(self):
        self.counter.remove()
        self.counter.remove()
        self.counter.remove()
        self.counter.remove()
        self.assertEqual(self.counter.get_value(), 0)

    def test_hard_input_two(self):
        for _ in range(0, 1000):
            self.counter.add()
        self.assertEqual(self.counter.get_value(), 1000)

    # It is complementary to setUp and is needed to put the object down after
    # the test.
    # It has to be executed at the end of the class
    def tearDown(self):
        # pass
        self.counter = None