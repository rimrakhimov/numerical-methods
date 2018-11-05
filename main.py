from math import exp
from controller import Controller

def f(x, y):
    res = y**2 * exp(x) - 2 * y
    if res == float('inf'):
        raise OverflowError
    return res

def y(x, x0, y0, eps):
    if (y0 == 0):
        return 0
    else:
        c = (1 - y0 * exp(x0)) / (y0 * exp(2 * x0))
        res = (exp(x) + c * exp(2 * x))
        resp = (exp(x + eps / 2) + c * exp(2 * (x + eps / 2)))
        resn = (exp(x - eps / 2) + c * exp(2 * (x - eps / 2)))
        if resp * resn < 0:
            return float('inf')
        return 1 / res

def main():
    Controller(f, y)

if __name__ == '__main__':
    main()