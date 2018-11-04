import numpy as np

class EulersMethod:

    @staticmethod
    def getValues(equation):
        f = equation.getf()
        y = equation.gety()
        x0 = equation.getx0()
        y0 = equation.gety0()
        X = equation.getX()
        N = equation.getN()
        h = EulersMethod.getStep(x0, X, N)

        xVal = np.array([(x0 + h * i) for i in range(N)])

        isInf = False
        res = [y0]
        isNeg = res[0] < 0
        for i in range(N-1):
            print(isNeg)
            if y(xVal[i], x0, y0) == float('inf'):
                isInf = True
                res.append(float('inf'))
            elif isInf:
                isInf = False
                res.append(y(xVal[i], x0, y0))
            elif (isNeg and y(xVal[i], x0, y0) > 0) or ((not isNeg) and y(xVal[i], x0, y0) < 0):
                res.append(y(xVal[i], x0, y0))
                isNeg = not isNeg
            else:
                res.append(res[i] + h*f(xVal[i], res[i]))

        yVal = np.array(res)

        return xVal, yVal

    @staticmethod
    def getStep(x0, X, N):
        return (X - x0) / N