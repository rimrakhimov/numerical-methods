from layout import MainWindow
from math import exp
from differential_equation import DifferentialEquation
from plot_builder import PlotBuilder
import wx

class Controller:
    def __init__(self, equation, solution):
        self.equation = equation
        self.solution = solution
        self.app = wx.App()
        self.mainFrame = MainWindow(self, None, id=wx.ID_ANY, title="Differential Equations",
                           style=wx.MINIMIZE_BOX | wx.CLOSE_BOX)
        self.mainFrame.Show()

        self.app.MainLoop()

    def OnSolutionButton(self, event):
        x0 = float(self.mainFrame.tcx0.GetValue())
        y0 = float(self.mainFrame.tcy0.GetValue())
        X = float(self.mainFrame.tcX.GetValue())
        N = int(self.mainFrame.tcN.GetValue())
        diff = DifferentialEquation(self.equation, x0, y0, X, N, self.solution)
        data = []
        methods = []
        if self.mainFrame.exactSolutionCheckBox.GetValue():
            values = diff.getExactSolution()
            if values is not None:
                data.append(values)
                methods.append('Exact Solution')

        if self.mainFrame.eulersMethodCheckBox.GetValue():
            values = diff.eulersMethodSolution()
            if values is not None:
                data.append(values)
                methods.append('Eulers Method')

        if self.mainFrame.improvedEulerMethodCheckBox.GetValue():
            values = diff.improveEulerMethodSolution()
            if values is not None:
                data.append(values)
                methods.append('Improved Euler Method')

        if self.mainFrame.rungeKuttaMethodCheckBox.GetValue():
            values = diff.rungeKuttaMethodSolution()
            if values is not None:
                data.append(values)
                methods.append('Runge-Kutta Method')
        if len(data) == 0:
            self.mainFrame.NotifyNothingToShow()
            event.Skip()
            return
        PlotBuilder.buildSolutionPlot(values=data, legend=methods)
        event.Skip()

    def OnLocalErrorButton(self, event):
        x0 = float(self.mainFrame.tcx0.GetValue())
        y0 = float(self.mainFrame.tcy0.GetValue())
        X = float(self.mainFrame.tcX.GetValue())
        N = int(self.mainFrame.tcN.GetValue())
        diff = DifferentialEquation(self.equation, x0, y0, X, N, self.solution)
        data = []
        methods = []

        exactValues = diff.getExactSolution()[1]

        if self.mainFrame.eulersMethodCheckBox.GetValue():
            values = diff.eulersMethodSolution()
            if values is not None:
                error = []
                for i in range(len(exactValues)):
                    if exactValues[i] != float('inf'):
                        error.append(abs(exactValues[i] - values[1][i]))
                    else:
                        error.append(float('inf'))
                data.append((values[0], error))
                methods.append('Eulers Method')

        if self.mainFrame.improvedEulerMethodCheckBox.GetValue():
            values = diff.improveEulerMethodSolution()
            if values is not None:
                error = []
                for i in range(len(exactValues)):
                    if exactValues[i] != float('inf'):
                        error.append(abs(exactValues[i] - values[1][i]))
                    else:
                        error.append(float('inf'))
                data.append((values[0], error))
                methods.append('Improved Euler Method')

        if self.mainFrame.rungeKuttaMethodCheckBox.GetValue():
            values = diff.rungeKuttaMethodSolution()
            if values is not None:
                error = []
                for i in range(len(exactValues)):
                    if exactValues[i] != float('inf'):
                        error.append(abs(exactValues[i] - values[1][i]))
                    else:
                        error.append(float('inf'))
                data.append((values[0], error))
                methods.append('Runge-Kutta Method')
        if len(data) == 0:
            self.mainFrame.NotifyNothingToShow()
            event.Skip()
            return

        PlotBuilder.buildLocalErrorPlot(values=data, legend=methods)
        event.Skip()

    def OnGlobalErrorButton(self, event):
        x0 = float(self.mainFrame.tcx0.GetValue())
        y0 = float(self.mainFrame.tcy0.GetValue())
        X = float(self.mainFrame.tcX.GetValue())
        NFrom = int(self.mainFrame.tcRangeFrom.GetValue())
        NTo = int(self.mainFrame.tcRangeTo.GetValue())
        data = [([], []), ([], []), ([], [])]
        for n in range(NFrom, NTo+1):
            diff = DifferentialEquation(self.equation, x0, y0, X, n, self.solution)

            exactValues = diff.getExactSolution()[1]

            if self.mainFrame.eulersMethodCheckBox.GetValue():
                values = diff.eulersMethodSolution()
                if values is not None:
                    data[0][0].append(n)
                    maxError = 0
                    for i in range(len(exactValues)):
                        if exactValues[i] != float('inf') and maxError < (abs(exactValues[i] - values[1][i])):
                            maxError = abs(exactValues[i] - values[1][i])
                    data[0][1].append(maxError)

            if self.mainFrame.improvedEulerMethodCheckBox.GetValue():
                values = diff.improveEulerMethodSolution()
                if values is not None:
                    data[1][0].append(n)
                    maxError = 0
                    for i in range(len(exactValues)):
                        if exactValues[i] != float('inf') and maxError < (abs(exactValues[i] - values[1][i])):
                            maxError = abs(exactValues[i] - values[1][i])
                    data[1][1].append(maxError)

            if self.mainFrame.rungeKuttaMethodCheckBox.GetValue():
                values = diff.rungeKuttaMethodSolution()
                if values is not None:
                    data[2][0].append(n)
                    maxError = 0
                    for i in range(len(exactValues)):
                        if exactValues[i] != float('inf') and maxError < (abs(exactValues[i] - values[1][i])):
                            maxError = abs(exactValues[i] - values[1][i])
                    data[2][1].append(maxError)

        methods = ['Eulers Method', 'Improved Euler Method', 'Runge-Kutta Method']
        if len(data[2][0]) == 0:
            data.pop(2)
            methods.pop(2)
        if len(data[1][0]) == 0:
            data.pop(1)
            methods.pop(1)
        if len(data[0][0]) == 0:
            data.pop(0)
            methods.pop(0)

        if len(methods) == 0:
            self.mainFrame.NotifyNothingToShow()
            event.Skip()
            return

        PlotBuilder.buildGlobalErrorPlot(values=data, legend=methods)
        event.Skip()

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