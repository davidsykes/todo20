import unittest
import sys
sys.path.append('../src')
sys.path.append('../../temperatures/Library/src')
from unittest.mock import MagicMock
from class_to_test import ClassToTest


class TestClassToTest(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_data()
        self.set_up_object_under_test()
        self.set_up_expectations()

    def test_1(self):
        self.assertTrue(False)


    # Support code

    def set_up_mocks(self):
        self.mock_1 = MagicMock()

    def set_up_data(self):
        self.date = 'data'

    def set_up_object_under_test(self):
        self.class_to_test = ClassToTest()

    def set_up_expectations(self):
        pass


