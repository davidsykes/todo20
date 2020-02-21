import re


class RestCommand(object):
    def __init__(self):
        self.Command = None
        self.Parameters = {}


class RestCommandParser(object):
    def __init__(self):
        self.url_regex = re.compile('^([a-z]+)\??([a-z]+=[a-z0-9]+)*$')
        self.param_regex = re.compile('^([a-z]+)=([a-z0-9]+)')

    def parse_rest_command(self, url):
        match = self.url_regex.match(url)
        if match:
            return self.make_command(match.groups())

    def make_command(self, groups):
        command = RestCommand()
        command.Command = groups[0]
        command.Parameters = self.extract_parameters(groups[1])
        return command

    def extract_parameters(self, group):
        parameters = {}
        if group is not None:
            match = self.param_regex.match(group)
            parameters[match.group(1)] = match.group(2)

        return parameters