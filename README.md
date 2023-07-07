# Monte Carlo Multivariate Integration

This file provides a python function to estimate the definite integral of a continuous bounded function.

# Background

This program uniformly draws points from the region of integration and calculates a sampled expected value of the function we are integrating. Then by multiplying the volume of our region of integration with the estimated expected value we get an estimate for the volume covered by our function.

Along with the estimation, the sample variance of the function is used to print an error bar of the estimation. The standard deviation is inversely proportional to the square root of the number of samples taken.

# Dependencies

While not needed NumPy or SymPy can be useful to define complex functions. The 'typing' module is imported to provide typing hints not supported in older versions of python and 'random' is used to help sample points.

# Examples
```python
import numpy as np #used for examples
>>> def f(vector): #Function to integrate
	x, y = vector
	return np.sin(x) * np.cos(y)
>>> reg = [(0, np.pi), (np.pi, 0)] #Region of integration
>>> est_integral(reg, f, 10**6)
#Returns in form of [approximation, error-bar]
>>> [0.00034858628582538, 0.002465702660602295]
```

# Notes

* This method (of sampling) is much faster than integrating the standard mathematical way using an extension of the classic Riemann sum method (for comparison my git also has an example of the Riemann method).

* The user can easily extend this to more complicated regions of integration but there is a trade off in error and run-time.

* This naive method of sampling can have a much higher variance than methods that use a distribution specific to the function to help draw points. This is particularly important since non-pathological high dimensional integrals tend to be very local. Many other Monte Carlo algorithms exist that aim to reduce the variance in different ways.