import numpy as np
from scipy.optimize import curve_fit
import math

def approximate_function(x):
    if x <= 25:
        # Linear ceil from 10 to 25
        return 25
    elif 25 < x <= 40:
        # Slow increase / plateau from 25 to 40
        return math.ceil(25 + 0.7 * (x - 25))
    else:
        # Faster increase from 40 to 70
        temp = math.ceil(27 + 0.9 * (x - 40))
        return min(temp, 40)
    
    

print(approximate_function(48))