import os
import sys

from contextlib import contextmanager

@contextmanager
def redirect_stdout(file=os.devnull):
    '''
    Prevent output to stdout.
    '''
    with open(file, 'w') as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

def to_time(time_delta):
    '''
    Return a formatted string from the time object passed.
    '''
    total_seconds = time_delta.seconds
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
