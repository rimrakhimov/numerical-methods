import numpy as np

class ImprovedEulerMethod:

    @staticmethod
    def getValues(equation):
        f = equation.getf()
        y = equation.gety()
        x0 = equation.getx0()
        y0 = equation.gety0()
        X = equation.getX()
        N = equation.getN()
        h = ImprovedEulerMethod.getStep(x0, X, N)

        xVal = np.array([(x0 + h * i) for i in range(N+1)])

        isInf = False
        yVal = [y0]
        try:
            for i in range(N):
                if y(xVal[i+1], x0, y0, h) == float('inf'):
                    isInf = True
                    yVal.append(float('inf'))
                elif isInf:
                    isInf = False
                    yVal.append(y(xVal[i+1], x0, y0, h))
                else:
                    k1 = f(xVal[i], yVal[i])
                    k2 = f(xVal[i] + h, yVal[i] + h * k1)
                    yVal.append(yVal[i] + h/2*(k1+k2))
        except OverflowError:
            return None

        yVal = np.array(yVal)

        return (xVal, yVal)

    @staticmethod
    def getStep(x0, X, N):
        return (X - x0) / N