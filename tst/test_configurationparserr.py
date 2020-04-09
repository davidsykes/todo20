import unittest
import sys
sys.path.append('../src')
sys.path.append('../../temperatures/Library/src')
from unittest.mock import MagicMock
from configurationparser import ConfigurationParser


class TestConfigurationParser(unittest.TestCase):
    def setUp(self):
        self.set_up_data()
        self.set_up_object_under_test()

    def test_parse_configuration_parses_configurations(self):
        config = self.parser.parse_configuration(self.get_config())
        self.assertEqual('value1', config['config1']['key1'])
        self.assertEqual('value2', config['config1']['key2'])
        self.assertEqual('value3', config['config2']['key1'])
        self.assertEqual('value4', config['config2']['key2'])

    def test_lines_with_no_header_come_under_a_global_key(self):
        self.data[0] = ''
        config = self.parser.parse_configuration(self.get_config())
        self.assertEqual('value1', config['global']['key1'])
        self.assertEqual('value2', config['global']['key2'])
        self.assertEqual('value3', config['config2']['key1'])
        self.assertEqual('value4', config['config2']['key2'])

    # Support code

    def set_up_data(self):
        self.data = ['[config1]','key1=value1','key2=value2','[config2]','key1=value3','key2=value4']

    def get_config(self):
        return "\n".join(self.data)

    def set_up_object_under_test(self):
        self.parser = ConfigurationParser()
