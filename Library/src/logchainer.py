

class LogChainer(object):
    def __init__(self, logger):
        self.loggers = [logger]

    def chain(self, logger):
        self.loggers.append(logger)

    def log(self, message):
        for logger in self.loggers:
            logger.log(message)

    def error(self, message):
        for logger in self.loggers:
            logger.error(message)
