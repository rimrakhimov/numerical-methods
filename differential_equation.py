from methods.exact_solution import ExactSolution
from methods.euler import EulersMethod
from methods.improved_euler import ImprovedEulerMethod
from methods.runge_kutta import RungeKuttaMethod

class DifferentialEquation:
    def __init__(self, f, x0, y0, X, N, y):
        self.f = f
        self.x0 = x0
        self.y0 = y0
        self.X = X
        self.N = N
        self.y = y

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
        values = ExactSolution.getValues(self)
        return values

    def eulersMethodSolution(self):
        values = EulersMethod.getValues(self)
        return values

    def improveEulerMethodSolution(self):
        values = ImprovedEulerMethod.getValues(self)
        return values

    def rungeKuttaMethodSolution(self):
        values = RungeKuttaMethod.getValues(self)
        return values