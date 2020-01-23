

class Logger(object):
    def __init__(self, factory, log_file, error_file):
        self.datetime_wrapper = factory.fetch('DateTimeWrapper')
        self.log_file = log_file
        self.error_file = error_file

    def log(self, message):
        self.log_file.write(self.format(message))

    def error(self, message):
        self.error_file.write(self.format(message))

    def format(self, message):
        current_date_and_time = self.datetime_wrapper.now().strftime('%Y-%m-%d %H:%M:%S')
        return '%s: %s%s' % (current_date_and_time, message, "\n")

