"""Estimate the definite integral of a continuous bounded function."""

import random
from typing import List #Not required for python 3.9 and above

def uniform(region: List[tuple], sigDigits=2) -> List[float]:
    """Uniformly draw a (multi-dimensional) point from a given region.

    Each coordinate of the point is rounded to 'sigDigits' decimal places.
    This can be changed for increased accuracy especially for tighter
    regions of integration but arithmetic on long digits will affect run-times.

    Parameters
    ----------
    region : List
        The region over which we draw points.
    sigDigits : int, optional
        Number of digits after each decimal point.
        
    Returns
    -------
    uniform(region, sigDigits) : List
        The randomly drawn point.
    
    """
    return [round(random.uniform(a, b), sigDigits) for a, b in region]

def sample_variance(sum_f: float, sum_sq: float, samples: int) -> float:
    """Calculate the sample variance.

    Parameters
    ----------
    sum_f : float
        Sum of evaluated randomly drawn points.
    sum_sq : float
        Sum of the square of evaluated randomly drawn points.
    samples : int
        The number of samples gathered.
        
    Returns
    -------
    sample_variance(sum_f, sum_sq, samples) : float
        The sample variance.

    """
    avg = sum_f / samples
    sum_errors = (sum_sq
                  - 2 * avg * sum_f
                  + samples * avg ** 2)
    
    return sum_errors / (samples - 1)

def error_bar(sample_space_vol: float, var_func: float, samples: int) -> float:
    """Calculate the error bar of our final answer.

    Parameters
    ----------
    sample_space_vol : float
        The volume of the region of integration.
    var_func : float
        The evaluated sample variance.
    samples : int
        The number of samples gathered.
        
    Returns
    -------
    error_bar(sample_space_vol, var_func, samples) : float
        The error-bar of our volume calculation.

    """
    return sample_space_vol * var_func / (samples ** .5)

def est_integral(region: List[tuple], function, samples: int) -> float:
    """Find the signed volume of the region of integration.

    Parameters
    ----------
    region : List
        Region of integration.
    function : robust to different types
        Multivariate function being integrated
    samples : int
        The number of samples to gather.
        
    Returns
    -------
    ans : List
        A list where the first entry is our estimated volume
        and second entry is the error bar of the calculation.
    
    """
    vol = 1
    for a, b in region:
        vol *= (b - a)
        
    sum_f = 0 #Used to aggregate evaluations of sampled points
    sum_f_squared = 0 #Used to aggregate squared evaluation of samples points

    for _ in range(samples):
        value = function(uniform(region))
        sum_f += value
        sum_f_squared += value ** 2

    #Calculate the sample average value of our function
    est_avg = sum_f / samples

    #By multiplying the volume of our region of integration
    #with the estimated expected value of our function over
    #the same region we get an estimate for the actual volume
    #f covers.
    result = vol * est_avg

    #Calculate the error bar for our estimation
    var_f = sample_variance(sum_f, sum_f_squared, samples)
    error = error_bar(vol, var_f, samples)

    ans = [result, error]
    
    return ans
