# helpers.py

import math

import math

def approximate_function(x):
    """
    Approximates the value of a function based on the input value x.

    Parameters:
    x (float): The input value for the function.

    Returns:
    float: The approximate value of the function.

    """
    if x <= 34:
        return 34
    elif 34 < x <= 50:
        return math.ceil(30 + 0.7 * (x - 34))
    else:
        temp = math.ceil(42 + 0.9 * (x - 50))
        return min(temp, 50)

def print_separator(char, length):
    print(char * length)

def print_job_info(title, info):
    print(f"{title}: {info}")
