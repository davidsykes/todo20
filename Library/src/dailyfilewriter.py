import atexit

# Open a dated file for writing
# Check each write for a change of day

class DailyFileWriter(object):
    def __init__(self, factory, file_name, file_extension):
        self.initialise_objects_from_factory(factory)
        self.file_name = file_name
        self.file_extension = file_extension
        self.current_file = None
        self.day_for_log = None
        atexit.register(self.cleanup)

    def write(self, text):
        self.ensure_file_for_today_is_open()
        self.current_file.write(text)
        self.current_file.flush()

    def initialise_objects_from_factory(self, factory):
        self.date_time_wrapper = factory.fetch('DateTimeWrapper')
        self.fs_wrapper = factory.fetch('FsWrapper')

    def ensure_file_for_today_is_open(self):
        day_for_log = self.get_day_for_log()
        if self.day_for_log_has_changed(day_for_log):
            self.close_current_file()
            self.open_file_for_today(day_for_log)

    def get_day_for_log(self):
        current_date_and_time = self.date_time_wrapper.now()
        day_for_log = self.get_date_from_today(current_date_and_time)
        return day_for_log

    def get_date_from_today(self, current_date_and_time):
        return current_date_and_time.strftime('%Y%m%d')

    def day_for_log_has_changed(self, day_for_log):
        return day_for_log != self.day_for_log

    def open_file_for_today(self, day_for_log):
        self.day_for_log = day_for_log
        filename = "%s_%s.%s" % (self.file_name, day_for_log, self.file_extension)
        self.current_file = self.fs_wrapper.open(filename, 'a')

    def cleanup(self):
        self.close_current_file()

    def close_current_file(self):
        if self.current_file:
            self.current_file.close()
