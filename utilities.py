import time
from time import mktime
from datetime import datetime


def combine_datetime(date, time_input):
    struct_datetime = time.strptime(date + ' ' + time_input, '%d %B, %Y %I:%M%p')
    final_datetime = datetime.fromtimestamp(mktime(struct_datetime))

    return final_datetime


def get_maps_key():
    with open('key.txt', 'r') as key_file:
        key = key_file.read()
    return key
