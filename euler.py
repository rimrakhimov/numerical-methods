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

        xVal = np.array([(x0 + h * i) for i in range(N+1)])

        isInf = False
        res = [y0]
        try:
            for i in range(N):
                if y(xVal[i+1], x0, y0, h) == float('inf'):
                    isInf = True
                    res.append(float('inf'))
                elif isInf:
                    isInf = False
                    res.append(y(xVal[i+1], x0, y0, h))
                else:
                    res.append(res[i] + h*f(xVal[i], res[i]))
        except OverflowError:
            print(h)
            print(list(zip(xVal, res)))

        yVal = np.array(res)

        return xVal, yVal

    @staticmethod
    def getStep(x0, X, N):
        return (X - x0) / N