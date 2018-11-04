from exact_solution import ExactSolution
from euler import EulersMethod
from improved_euler import ImprovedEulerMethod

class DifferentialEquation:
    def __init__(self, f, x0, y0, X, N, y):
        self.f = f
        self.x0 = x0
        self.y0 = y0
        self.X = X
        self.N = N
        self.y = y

    def setInitialValues(self, x0, y0, y):
        self.x0 = x0
        self.y0 = y0

    def setX(self, X):
        self.X = X

    def setN(self, N):
        self.N = N

    def getf(self):
        return self.f

    def gety(self):
        return self.y

    def getX(self):
        return self.X

    def getx0(self):
        return self.x0

    def gety0(self):
        return self.y0

    def getN(self):
        return self.N

    def getExactSolution(self):
        xVal, yVal = ExactSolution.getValues(self)
        return xVal, yVal

    def eulersMethodSolution(self):
        xVal, yVal = EulersMethod.getValues(self)
        return xVal, yVal

    def improveEulerMethodSolution(self):
        xVal, yVal = ImprovedEulerMethod.getValues(self)
        return xVal, yVal