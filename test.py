from differential_equation import DifferentialEquation
from math import exp
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return y**2 * exp(x) - 2 * y

def y(x, x0, y0, eps=10**(-1)):
    if (y0 == 0):
        return 0
    else:
        c = (1 - y0 * exp(x0)) / (y0 * exp(2*x0))
        res = (exp(x) + c * exp(2*x))
        if abs(res) < eps:
            resp = (exp(x+1) + c * exp(2*(x+1)))
            resn = (exp(x-1) + c * exp(2*(x-1)))
            if resp*resn < 0:
                return float('inf')
        return 1 / res

diff = DifferentialEquation(f, 1, 1, 10, 50, y)

xVal, yVal = diff.getExactSolution()
# xVal, yVal = diff.eulersMethodSolution()
# xVal, yVal = diff.improveEulerMethodSolution()

plt.plot(xVal, yVal, label='linear')
plt.show()

# print(y(3.16, 1, 1))eps=10**(-1)