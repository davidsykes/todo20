import re

class ConfigurationParserWorkingSet(object):
    def __init__(self):
        self.lines = None
        self.header = None
        self.values = None


class ConfigurationParser(object):
    def __init__(self):
        self.regex_header = re.compile('^\[([a-zA-Z0-9]+)\]$')
        self.regex_value = re.compile('^([a-zA-Z0-9]+)=(.+)$')

    def parse_configuration(self, config):
        working_set = self.create_working_set(config)
        for line in working_set.lines:
            match = self.regex_header.match(line)
            if match:
                self.update_header(working_set, match.group(1))
            else:
                match = self.regex_value.match(line)
                if match:
                    self.create_header_if_required(working_set)
                    self.add_value(working_set, match.groups())
        return working_set.values

    def create_working_set(self, config):
        working_set = ConfigurationParserWorkingSet()
        working_set.lines = config.splitlines(False)
        working_set.header = 'global'
        working_set.values = {}
        return working_set

    def update_header(self, working_set, header):
        working_set.header = header

    def create_header_if_required(self, working_set):
        if working_set.header not in working_set.values:
            working_set.values[working_set.header] = {}

    def add_value(self, working_set, groups):
        working_set.values[working_set.header][groups[0]] = groups[1]