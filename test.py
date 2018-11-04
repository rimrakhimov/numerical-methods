from differential_equation import DifferentialEquation
from math import exp
import matplotlib.pyplot as plt

def f(x, y):
    return y**2 * exp(x) - 2 * y

def y(x, x0, y0, eps):
    if (y0 == 0):
        return 0
    else:
        c = (1 - y0 * exp(x0)) / (y0 * exp(2*x0))
        res = (exp(x) + c * exp(2*x))
        resp = (exp(x+eps/2) + c * exp(2*(x+eps/2)))
        resn = (exp(x-eps/2) + c * exp(2*(x-eps/2)))
        if resp*resn < 0:
            return float('inf')
        return 1 / res

diff = DifferentialEquation(f, 1, 1, -5, 30, y)

xVal, yVal = diff.getExactSolution()
print(list(zip(xVal, yVal)))
xVal, yVal = diff.eulersMethodSolution()
print("Euler")
print(list(zip(xVal, yVal)))
xVal, yVal = diff.improveEulerMethodSolution()
print("Improve:")
print(list(zip(xVal, yVal)))
xVal, yVal = diff.rungeKuttaMethodSolution()
print(list(zip(xVal, yVal)))


# plt.plot(xVal, yVal, label='linear')
# plt.show()

# print(y(3.16, 1, 1))eps=10**(-1)