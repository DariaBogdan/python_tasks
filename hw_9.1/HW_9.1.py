#!/usr/bin/env python3.6
import datetime
import time


class SaveExceptionInfo:
    """Сontext manager saves info into file about exception,
    current time, execution time by rewriting given file.
    """
    def __init__(self, filename):
        """Saves filename"""
        self.filename = filename

    def __enter__(self):
        """Saves start time"""
        self.start_time = datetime.datetime.now()

    def __exit__(self, *args):
        """If error occurred, rewrites file with info about error"""
        if sum(map(bool, args)):  # if error occurred, args are not None

            # collect some info about error
            error_info = "; ".join([str(arg) for arg in args])
            current_time = datetime.datetime.now()
            time_executed =  current_time - self.start_time

            # write info to file
            self.open_file = open(self.filename, 'w')
            self.open_file.write(f'Error occurкed: {error_info}\n'
                                 f'Time executed: {time_executed}\n'
                                 f'Current time: {current_time}\n')
            self.open_file.close()


if __name__ == '__main__':
    array = list(range(2))
    with SaveExceptionInfo('foo.txt'):
        time.sleep(1)
        for index in range(3):
            print(array[index])