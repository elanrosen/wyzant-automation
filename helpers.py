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
    if x <= 55:
        return 55
    elif 55 < x:
        temp =  math.ceil(55 + 0.9 * (x - 55))
        return min(temp, 70)

def print_separator(char, length):
    print(char * length)

def print_job_info(title, info):
    print(f"{title}: {info}")
