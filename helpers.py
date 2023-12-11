# helpers.py

import math

def approximate_function(x):
    if x <= 25:
        return 25
    elif 25 < x <= 40:
        return math.ceil(25 + 0.7 * (x - 25))
    else:
        temp = math.ceil(27 + 0.9 * (x - 40))
        return min(temp, 40)

def print_separator(char, length):
    print(char * length)

def print_job_info(title, info):
    print(f"{title}: {info}")
