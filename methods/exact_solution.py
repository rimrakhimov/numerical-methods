import numpy as np

class ExactSolution:
    # def __init__(self, equation):
    #     self.equation = equation

    @staticmethod
    def getValues(equation):
        y = equation.gety()
        x0 = equation.getx0()
        y0 = equation.gety0()
        X = equation.getX()
        N  = equation.getN()
        h = ExactSolution.getStep(x0, X, N)

        xVal = np.array([(x0 + h*i) for i in range(N+1)])
        yVal = np.array([y(i, x0, y0, h) for i in xVal])

        return (xVal, yVal)

    @staticmethod
    def getStep(x0, X, N):
        return (X - x0) / N