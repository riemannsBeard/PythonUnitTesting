import sys
import unittest
from io import StringIO
from third_project import Profile


class TestPrintedOutPut(unittest.TestCase):

    def setUp(self):
        # First line is waiting for any console printed output
        # Once done, it is stored in sys.stdout
        self.held, sys.stdout = sys.stdout, StringIO()
        self.profile = Profile('Antonio', 35, 'engineer')

    def test_name(self):
        self.profile.print_name()
        # The method sys.stdout.getvalue() gets the value of the string that
        # was printed out in the console. The method strip() avoids the
        # previous method to insert an extra newline
        self.assertEqual(sys.stdout.getvalue().strip(), 'Antonio')

    def test_age(self):
        self.profile.print_age()
        # Need to cast the argument passed to the method because
        # sys.stdout.getvalue().strip() returns a string
        self.assertEqual(sys.stdout.getvalue().strip(), str(35))

    def test_job(self):
        self.profile.print_job()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Engineer')

    def tearDown(self):
        self.profile = None




























