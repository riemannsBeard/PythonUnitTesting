import unittest
from first_challenge import counter

class EasyTestCase(unittest.TestCase):
    def test_easy_input(self):
        # Todo: make sure that your program returns 2 given the string 'Mo'
        # pass
        self.assertEqual(counter('Mo'), 2)

    def test_easy_input_two(self):
        # Todo: make sure that your program returns 8 given the string 'Mohammad'
        # pass
        self.assertEqual(counter('Mohammad'), 8)


class MediumTestCase(unittest.TestCase):
    def test_medium_input(self):
        # Todo: make sure that the program raises an exception whenever there is any non-english charts. Ex. !@#$%^.
        with self.assertRaises(Exception):
            self.assertEqual(counter('Mo@!^'), 2)

    def test_medium_input_two(self):
        # Todo: make sure that your program does not count spaces. It should
        #  only count english alpha.
        self.assertEqual(counter('Antonio Martin'), 13)


class HardTestCase(unittest.TestCase):
    def test_hard_input(self):
        # Todo: make sure that the program raises an exception whenever an empty string is given.
        with self.assertRaises(Exception):
            self.assertEqual(counter(' '), 0)

    def test_hard_input_two(self):
        # Todo: make sure that your program does not accept a None input.
        with self.assertRaises(AttributeError):
            self.assertEqual(counter(None), 0)


if __name__ == '__main__':
    unittest.main()
