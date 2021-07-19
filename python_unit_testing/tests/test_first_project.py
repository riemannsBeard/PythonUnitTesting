import unittest
from first_project import avg

class EasyTestCase(unittest.TestCase):

    def test_easy_input(self):
        self.assertEqual(avg(1, 2, 3), 2)

    def test_easy_input_two(self):
        self.assertEqual(avg(10, 10, 10, 10, 10), 10)

class MediumTestCase(unittest.TestCase):

    def test_medium_input(self):
        # If this line of code is throwing a TypeError, then this means that
        # this test passed, and the function is doing what it is supposed to do
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, "Antonio"), 2)

    def test_medium_input_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(10, 10, 10, 10, "10"), 10)


class HardTestCase(unittest.TestCase):

    def test_hard_input(self):
        # If this line of code is throwing a TypeError, then this means that
        # this test passed, and the function is doing what it is supposed to do
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, None), 2)

    def test_hard_input_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(10, 10, 10, 10, float), 10)

    def test_hard_input_three(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(10, 10, 10, 10, frozenset), 10)

    def test_hard_input_four(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(10, 10, 10, 10, set), 10)

# Is that this file being run directly by Python or is it being imported?
if __name__ == '__main__':
    unittest.main()