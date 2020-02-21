import unittest
import sys
sys.path.append('../src')
from unittest.mock import MagicMock
from restcommandparser import RestCommandParser

class TestRestCommandParser(unittest.TestCase):
    def setUp(self):
        self.set_up_object_under_test()

    def test_simple_command_is_parsed(self):
        cmd = self.parser.parse_rest_command('todo')
        self.assertEqual('todo', cmd.Command)

    def test_if_no_parameters_are_supplied_parameters_parameter_is_empty(self):
        cmd = self.parser.parse_rest_command('todo')
        self.assertEqual(0, len(cmd.Parameters))

    def test_single_parameters_are_parsed(self):
        cmd = self.parser.parse_rest_command('todo?parama=one')
        self.assertEqual('todo', cmd.Command)
        self.assertEqual(1, len(cmd.Parameters))
        self.assertEqual('one', cmd.Parameters['parama'])

    # def test_multiple_parameters_are_parsed(self):
    #     cmd = self.parser.parse_rest_command('todo?parama=one&paramb=2')
    #     self.assertEqual('todo', cmd.Command)
    #     self.assertEqual(2, len(cmd.Parameters))
    #     self.assertEqual('one', cmd.Parameters['parama'])
    #     self.assertEqual('2', cmd.Parameters['paramb'])

    def test_non_alpha_commands_are_ignored(self):
        cmd = self.parser.parse_rest_command('todo2')
        self.assertIsNone(cmd)

    def test_parameters_with_non_alpha_names_are_ignored(self):
        cmd = self.parser.parse_rest_command('todo?param1=one')
        self.assertIsNone(cmd)

    def test_parameters_with_non_alphanumeric_values_are_ignored(self):
        cmd = self.parser.parse_rest_command('todo?param=w$e')
        self.assertIsNone(cmd)

    # Support code

    def set_up_object_under_test(self):
        self.parser = RestCommandParser()

